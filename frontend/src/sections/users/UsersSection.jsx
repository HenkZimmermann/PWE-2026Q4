import { useEffect, useState } from "react";
import { getAllUsers } from "../../api/user";
import userStatistics from "../../page/UserStatistics"
import UserCard from "../../page/UserCard";
import "./UsersSection.css";
import ProfileStats from "../../page/UserStatistics";
import { useParams } from "react-router-dom";

function Element() {
    const [users, setUsers] = useState(null);
    const [error, setError] = useState(false);
    console.log(users)

    // Benutzer aus dem Backend laden
    useEffect(() => {
        let active = true;

        getAllUsers()
            .then((users) => {
                if (active)
                    setUsers(users);
            })
            .catch((error) => {
                if (active) {
                    console.error(error);
                    setError(true);
                }
            });

        return () => {
            active = false;
        };
    }, []);

    return (
        /* Main Div in dem alle User als Card angezeit werden */
        <div className="users-section">
            <h1>Benutzer</h1>
            {users === null && !error && (
                <p role="status">Benutzer werden geladen...</p>
            )}
            {/* Fehler beim Laden */}
            {error && (
                <p role="alert">Benutzer konnten nicht geladen werden.</p>
            )}
            {/* Keine Benutzer vorhanden */}
            {users?.length === 0 && (
                <p role="status">Es gibt noch keine Benutzer.</p>
            )}
            {/* Benutzer anzeigen */}
            <div className="users-grid">
                {users?.map((user) => (
                    <UserCard key={user.id} user={user} />
                ))}
            </div>
        </div>
    );
}

/* User Stats für den jeweiligen User */
function UserDetail() {
    const { userId } = useParams();

    return (
        <div className="profile">
            <h2 className="profile-card-title">Statistiken</h2>
            <section className="profile-card">
                <ProfileStats userId={userId} />
            </section>
        </div>
    );
}
export const UsersSection = {
    title: "Benutzer",
    icon: "👥",
    url: "/users",
    /* Einbinden der Routes für die Stats der User */
    subUrls: [
        { url: "/users/:userId", element: <UserDetail /> }
    ],
    showInSidebar: true,
    element: <Element />
};

export default UsersSection;