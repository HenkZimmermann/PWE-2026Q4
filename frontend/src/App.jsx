import { useEffect } from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import ConnectionMonitor from "./page/ConnectionMonitor";
import ThreadDetail from "./page/ThreadDetail";
import Sections from "./sections/Sections"
import Sidebar from "./page/Sidebar"
import "./App.css"

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

    // Scroll zurücksetzen, wenn Section gewechselt wird
    useEffect(() => {
        window.scrollTo(0, 0);
    }, [pathname]);

    return (
        <div className="app-layout">
            <Sidebar />
            <main className="main-content">
                <RouteRegistration />
            </main>
            <ConnectionMonitor />
        </div>
    );
}

export default App;
