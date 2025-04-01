import { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";
import { auth } from "/Users/vishnu/Desktop/agri_project/frontend/src/firebaseConfig";  

const PrivateRoute = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((currentUser) => {
      setUser(currentUser);
      setLoading(false);
    });

    return () => unsubscribe(); // Cleanup listener
  }, []);

  if (loading) return <div>Loading...</div>; // Show loading state

  return user ? children : <Navigate to="/" />;
};

export default PrivateRoute;
