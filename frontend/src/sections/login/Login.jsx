import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { requestLogin, requestUserData } from "../../api/login";
import { useUser } from "../../context/UserProvider";
import "./Login.css";


const LoginSection = () => {
    const { setUser } = useUser();
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [pwd, setPwd] = useState("");
    const [errMsg, setErrMsg] = useState("");


    const submitLogin = async (e) => {
        e.preventDefault();

        try {
            // Login Credentials an Backend übermitteln
            const accessToken = await requestLogin(email,pwd)
            // Acces Token im Local Storage speichern
            localStorage.setItem("accessToken", accessToken);
            // Userdaten per Acces Token abrufen und zwischenspeichern
            const userData = await requestUserData(accessToken)
            // Rollenname statt ID speichern
            let roleName;
            switch (Number(userData.role)) {
                case 1:
                    roleName = "Admin";
                    break;
                case 2:
                    roleName = "Moderator";
                    break;
                case 3:
                    roleName = "User";
                    break;
            }
            setUser({
                    username: userData.username,
                    id: userData.user_id,
                    email: userData.email,
                    role: roleName,
                    roleId: userData.role
            })

            navigate("/", { replace: true });
        } catch (err) {
            setErrMsg(err instanceof Error ? err.message : "Anmeldung fehlgeschlagen.");        
        }
    };

    return (
        <section className="login-card">
            <p
                className={errMsg ? "errmsg" : "offscreen"}
            >
                {errMsg}
            </p>

            <h1>Forum Login</h1>

            <form onSubmit={submitLogin}>
                <label htmlFor="email">
                    E-Mail:
                </label>
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
            <p>
                Noch kein Benutzer? <Link to="/register">!Klick mich!</Link>
            </p>
        </section>
    );
};

export default LoginSection;