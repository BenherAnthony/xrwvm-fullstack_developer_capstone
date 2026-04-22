import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";
import Home from "./components/Home/Home";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      {/* Home (NEW) */}
      <Route path="/" element={<Home />} />

      {/* Login */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;