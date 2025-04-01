import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyA9Ocag-1pdgRsA2w1MlQhDAUWbPEh794M",
    authDomain: "agriapp-aae9e.firebaseapp.com",
    projectId: "agriapp-aae9e",
    storageBucket: "agriapp-aae9e.firebasestorage.app",
    messagingSenderId: "399428152963",
    appId: "1:399428152963:web:da0556fe4ad59f37aef5b6"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
const db = getFirestore(app);

export { auth, provider, db };

export default app;
