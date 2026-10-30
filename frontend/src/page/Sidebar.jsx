import { Link } from "react-router-dom"
import Sections from "../sections/Sections"
import "./Sidebar.css"

export function Sidebar() {
    return (
        <aside className="sidebar">
            <div className="sidebar-header">
                <h2>PWE-2026Q4 Forum</h2>
            </div>
            <nav>
                <ul>
                    {Sections.map((section) => (
                        <li key={section.url}>
                            <Link to={section.url}>{section.title}</Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </aside>
    );
}

export default Sidebar;