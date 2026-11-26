import { useState,  } from "react";
import { useNavigate } from "react-router-dom";
import {  requestRegistration } from "../../api/register";
import "./Register.css";


const LoginSection = () => {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [pwd, setPwd] = useState("");
    const [errMsg, setErrMsg] = useState("");


    const submitRegistration = async (e) => {
        e.preventDefault();
        setErrMsg("");
        try {
            // Registration Infos an Backend übermitteln
            const created = await requestRegistration(username,email,pwd)
            setErrMsg(created?"User erfolgreich registriert":"Diese E-Mail Adresse ist bereits registriert")
            if (created){
                navigate("/login", { replace: true });
            }
            else{
                setErrMsg("Diese E-Mail Adresse ist bereits registriert")
            }
        } catch (err) {
            setErrMsg(err instanceof Error ? err.message : "Anmeldung fehlgeschlagen.");        
        }
    };

    return (
        <section className="registration-card">
            <p
                className={errMsg ? "errmsg" : "offscreen"}
            >
                {errMsg}
            </p>

            <h1>Forum Registration</h1>

            <form onSubmit={submitRegistration}>
                <label htmlFor="username">Benutername:</label>
                <input
                    type="text"
                    id="username"
                    autoComplete="username"
                    onChange={(e) => setUsername(e.target.value)}
                    value={username}
                    required
                />
                <label htmlFor="email">E-Mail:</label>
                <input
                    type="email"
                    id="email"
                    autoComplete="email"
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                    required
                />

                <label htmlFor="password">Passwort:</label>
                <input
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    onChange={(e) => setPwd(e.target.value)}
                    value={pwd}
                    required
                />

                <button type="submit">Login</button>
            </form>
        </section>
    );
};

export default LoginSection;