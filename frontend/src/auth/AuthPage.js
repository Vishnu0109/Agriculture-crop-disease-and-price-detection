import React, { useState, useEffect } from "react";
import { auth, provider, db } from "/Users/vishnu/Desktop/agri_project/frontend/src/firebaseConfig";
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, signOut, onAuthStateChanged } from "firebase/auth";
import { doc, setDoc } from "firebase/firestore";
import { useNavigate } from "react-router-dom";

const AuthPage = () => {
  const navigate = useNavigate();
  const [isSignUp, setIsSignUp] = useState(true);
  const [darkMode, setDarkMode] = useState(localStorage.getItem("darkMode") === "enabled");
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // 🔄 Add Loading State

  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    mobile: "",
    gender: "Male",
  });

  // ✅ Check if user is already logged in
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      setLoading(false); // ⏳ Stop loading once we get user info
      if (currentUser) navigate("/dashboard"); // 🚀 Redirect to dashboard if logged in
    });

    return () => unsubscribe(); // Cleanup listener
  }, [navigate]);

  const toggleDarkMode = () => {
    setDarkMode((prevMode) => !prevMode);
    localStorage.setItem("darkMode", darkMode ? "disabled" : "enabled");
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // ✅ Handle Email/Password Signup & Login
  const handleAuth = async (e) => {
    e.preventDefault();
    const { firstName, lastName, email, password, mobile, gender } = formData;

    try {
      if (isSignUp) {
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;

        await setDoc(doc(db, "users", user.uid), { firstName, lastName, email, mobile, gender });

        alert("User signed up successfully!");
      } else {
        await signInWithEmailAndPassword(auth, email, password);
        alert("User logged in successfully!");
        navigate("/dashboard");
      }
    } catch (error) {
      console.error("Error:", error);
      alert(error.message);
    }
  };

  // ✅ Handle Google Authentication
  const handleGoogleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;

      const userRef = doc(db, "users", user.uid);
      await setDoc(userRef, {
        firstName: user.displayName?.split(" ")[0] || "",
        lastName: user.displayName?.split(" ")[1] || "",
        email: user.email,
        mobile: user.phoneNumber || "",
        gender: "Not Specified",
      }, { merge: true });

      alert("Google Sign-In successful!");
      navigate("/dashboard");
    } catch (error) {
      console.error("Google Sign-In Error:", error);
      alert(error.message);
    }
  };

  // ✅ Handle Logout
  const handleLogout = async () => {
    try {
      await signOut(auth);
      setUser(null);
      alert("Logged out successfully!");
      navigate("/");
    } catch (error) {
      console.error("Logout Error:", error);
      alert(error.message);
    }
  };

  if (loading) {
    return <div className="flex justify-center items-center min-h-screen text-white">Loading...</div>;
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-green-400 to-blue-500 dark:bg-gray-900">
      {/* 🌑 Dark Mode Toggle */}
      <button onClick={toggleDarkMode} className="dark-mode-toggle absolute top-4 right-4 text-gray-700 dark:text-white">
        {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
      </button>

      <div className="auth-box floating bg-white dark:bg-gray-800 p-8 rounded-lg shadow-lg w-96">
        <h2 className="auth-title fade-in text-3xl font-semibold text-center text-gray-700 dark:text-white mb-4">
          {user ? `Welcome, ${user.displayName || user.email}` : isSignUp ? "Create Account" : "Welcome Back!"}
        </h2>

        {user ? (
          <button onClick={handleLogout} className="btn-primary w-full">
            Logout
          </button>
        ) : (
          <form onSubmit={handleAuth} className="space-y-4 fade-in">
            {isSignUp && (
              <>
                <input type="text" name="firstName" placeholder="First Name" value={formData.firstName} onChange={handleChange} className="input-style" required />
                <input type="text" name="lastName" placeholder="Last Name" value={formData.lastName} onChange={handleChange} className="input-style" required />
                <input type="text" name="mobile" placeholder="Mobile Number" value={formData.mobile} onChange={handleChange} className="input-style" required />
                <select name="gender" value={formData.gender} onChange={handleChange} className="input-style" required>
                  <option>Male</option>
                  <option>Female</option>
                  <option>Others</option>
                </select>
              </>
            )}

            <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} className="input-style" required />
            <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} className="input-style" required />

            <button type="submit" className="btn-primary w-full">
              {isSignUp ? "Sign Up" : "Sign In"}
            </button>
          </form>
        )}

        {!user && (
          <>
            {/* 🔥 Google Sign-In Button */}
            <button
              type="button"
              onClick={handleGoogleSignIn}
              className="w-full flex items-center justify-center gap-2 bg-red-500 text-white py-2 rounded-md hover:bg-red-600 transition mt-4">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/512px-Google_%22G%22_Logo.svg.png"
                   alt="Google Logo"
                   className="w-5 h-5" />
              Sign in with Google
            </button>

            <p className="text-center mt-4">
              {isSignUp ? "Already have an account?" : "New here?"}{" "}
              <button onClick={() => setIsSignUp(!isSignUp)} className="text-blue-500 dark:text-green-300">
                {isSignUp ? "Sign In" : "Sign Up"}
              </button>
            </p>
          </>
        )}
      </div>
    </div>
  );
};

export default AuthPage;
