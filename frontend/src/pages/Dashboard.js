import React from "react";
import { useNavigate } from "react-router-dom";
import { auth } from "/Users/vishnu/Desktop/agri_project/frontend/src/firebaseConfig";
import { signOut } from "firebase/auth";

const Dashboard = () => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    await signOut(auth);
    navigate("/");
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl font-bold mb-4">Welcome to the Dashboard</h1>
      <button
        onClick={handleLogout}
        className="px-4 py-2 bg-red-500 text-white rounded"
      >
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
