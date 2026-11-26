import { useState } from "react";
import { NavLink } from "react-router-dom"
import { useUser } from "../context/UserProvider";
import Sections from "../sections/Sections"
import "./Sidebar.css"

export function Sidebar() {
    //Username aus Zwischenspeicher (UserProvider) holen
    const { user, setUser } = useUser();
    const [failedAvatar, setFailedAvatar] = useState(null);
    
    const displayName = user?.username|| "Profil";
    const avatarUrl = user?.avatarUrl || "/profile-default.png";

    function logout() {
        const confirmed = window.confirm("Möchtest du dich wirklich abmelden?");
        // AccessToken aus lokalem Speicher löschen
        if (confirmed) {
            localStorage.removeItem("accessToken");
            setUser(null);
        }
    }
    return (
        <aside className="sidebar">
            <div className="sidebar-header">
                <img src="/forum-logo.png" width="36" height="36" alt="" />
                <h2>PWE-Forum</h2>
            </div>
            <nav>
                <ul>
                    {Sections.filter(section => section.showInSidebar).map((section) => (
                        <li key={section.url}>
                            <NavLink to={section.url}>
                                <span>{section.icon}</span>
                                {section.title}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </nav>
            {user && (
                <button
                    type="button"
                    className="sidebar-profile"
                    onClick={logout}
                >
                    <span className="sidebar-avatar" aria-hidden="true">
                        {failedAvatar === avatarUrl ? (
                            displayName.charAt(0).toUpperCase()
                        ) : (
                            <img
                                src={avatarUrl}
                                alt=""
                                onError={() => setFailedAvatar(avatarUrl)}
                            />
                        )}
                    </span>
                    <span className="sidebar-profile-text">
                        <strong>{displayName}</strong>
                        <span>{user.email}</span>
                    </span>

                </button>
            )}
        </aside>
    );
}

export default Sidebar;
