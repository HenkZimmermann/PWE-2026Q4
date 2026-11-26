import { useEffect, useState } from "react";
import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import ConnectionMonitor from "./page/ConnectionMonitor";
import ThreadDetail from "./page/ThreadDetail";
import LoginSection  from "./sections/login/Login";
import RegisterSection from "./sections/register/Register"
import { requestUserData } from "./api/login";
import { useUser } from "./context/UserProvider";
import Sections from "./sections/Sections";
import Sidebar from "./page/Sidebar";
import "./App.css";

function RouteRegistration() {
    return (
        <Routes>
            <Route path="/threads/:threadId" element={<ThreadDetail />} />

            // Section URLs als Route registrieren
            {Sections.map((section) => (
                <Route key={section.url} path={section.url} element={section.element} />
            ))}

            // Die Sub-URLs der Section auch als Route registrieren
            {Sections.map((section) =>
                section.subUrls?.map((subUrl) => (
                    <Route key={subUrl.url} path={subUrl.url} element={subUrl.element} />
                ))
            )}
        </Routes>
    );
}

function App() {
    const {pathname} = useLocation();
    const {user, setUser} = useUser();
    const [isChecking, setIsChecking] = useState(true);
    // Scroll zurücksetzen, wenn Section gewechselt wird
    useEffect(() => {
        window.scrollTo(0, 0);
    }, [pathname]);
    useEffect(()=>{
        let active = true;
        // Login bei aktivem Token wiederherstellen
        async function restoreLogin() {
            try {
                // Access Token abfragen
                const token = localStorage.getItem("accessToken");
                if (!token) {
                    setUser(null);
                    return;
                }
                // Abfragen der User Data per Token. Automatische validierung des Token vom Backend
                const userData = await requestUserData(token)
                if(active){
                    // Setzen der Attribute im Userprovider (Zwischenspeicher)
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
                    // Userdaten zwischenspeichern
                    setUser({
                            username: userData.username,
                            id: userData.user_id,
                            email: userData.email,
                            role: roleName 
                    })
                }
            } catch (error) {
                if (active) {
                    console.error(error);
                    setUser(null);
                }
            } finally {
                if (active) {
                    setIsChecking(false);
                }
            }
        }
        restoreLogin();
        return () => {
            active = false;
        };
    }, [setUser]);
    // Bei erstmaligem aufrufen wenn ggf. noch ein Access Token gespeichert ist
    if (isChecking) {
        return <p>Anmeldung wird geprüft …</p>;
    }

     return (
        // erst auf die Forum Routen weiterleiten wenn der User authentifiziert ist
        // Registrierung auch für nicht authentifizierte Benutzer erreichbar
        <Routes>
            <Route
                path="/login"
                element={user ? <Navigate to="/" replace /> : <LoginSection />}
            />
            <Route
                path="/register"
                element={user ? <Navigate to="/" replace /> : <RegisterSection />}
            />
            <Route
                path="*"
                element={
                    user ? (
                        <div className="app-layout">
                            <Sidebar />
                            <main className="main-content">
                                <RouteRegistration />
                            </main>
                            <ConnectionMonitor />
                        </div>
                    ) : (
                        <Navigate to="/login" replace />
                    )
                }
            />
        </Routes>
    );
}

export default App;
