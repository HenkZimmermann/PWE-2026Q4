import { Routes, Route } from "react-router-dom";
import Sections from './sections/Sections'

function RouteRegistration() {
    return (
        <Routes>
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
    return (
        <div className="app-layout">
            <main className="main-content">
                <RouteRegistration />
            </main>
        </div>
    );
}

export default App;