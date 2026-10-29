import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Sections from './sections/Sections'

function AppInner() {
    return (
        <div className="page-shell">
            <Routes>
                {Sections.map((section) => (
                    <Route key={section.url} path={section.url} element={section.element} />
                ))}
                {Sections.map((section) =>
                    section.subUrls?.map((subUrl) => (
                        <Route key={subUrl.url} path={subUrl.url} element={subUrl.element} />
                    ))
                )}
            </Routes>
        </div>
    );
}

function App() {
    return (
        <BrowserRouter>
            <AppInner />
        </BrowserRouter>
    );
}

export default App;