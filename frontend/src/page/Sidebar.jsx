import { Link } from "react-router-dom"
import Sections from "../sections/Sections"
import "./Sidebar.css"

export function Sidebar() {
    return (
        <aside className="sidebar">
            <div className="sidebar-header">
                <h2>PWE-Forum</h2>
            </div>
            <nav>
                <ul>
                    {Sections.filter(section => section.showInSidebar).map((section) => (
                        <li key={section.url}>
                            <Link to={section.url}>
                                <span>{section.icon}</span>
                                {section.title}
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </aside>
    );
}

export default Sidebar;