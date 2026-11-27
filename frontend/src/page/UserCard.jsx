
import { Link } from "react-router-dom";
import "./UserCard.css";

// Initialien aus Benutername bilden (für Profilfoto auf Card)
function getInitials(username) {
    return username.trim().split(/\s+/)
        .slice(0, 2)
        .map(part => part[0])
        .join("")
        .toUpperCase();
}

// Card für den jeweiligen User anlegen
export default function UserCard({ user }) {
    return (
        <article className="user-card">
            <header className="user-card-header">
                <div className="user-card-avatar">
                    {getInitials(user.username)}
                </div>

                <div className="user-card-info">
                    <h2>
                        {/* Verlinung auf die User Stats */}
                        <Link to={`/users/${user.id}`}>{user.username}</Link>
                    </h2>
                </div>
            </header>

            <div className="user-card-stats">
                <div className="user-card-stat">
                    <strong>{user.threadCount ?? 0}</strong>
                    <span>Threads</span>
                </div>
                <div className="user-card-stat">
                    <strong>{user.commentCount ?? 0}</strong>
                    <span>Kommentare</span>
                </div>
            </div>

            <footer className="user-card-group">
                <span>Aktivste Gruppe</span>
                <strong>{user.mostActiveGroupName ?? "Keine Gruppe"}</strong>
            </footer>
        </article>
    );
}