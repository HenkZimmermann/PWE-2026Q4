import { useEffect, useState } from "react";
import { useUser } from "../../context/UserProvider";
import { editUser, deleteUser } from "../../api/user";
import EditProfileDialog from "../../page/EditProfileDialog.jsx"
import FloatingActionButton from "../../page/FloatingActionButton";
import "./ProfileSection.css";
import ProfileStats from "../../page/UserStatistics.jsx";

function Element() {
    const {user,setUser} = useUser();
    
    const [showEditForm, setShowEditForm] = useState(false);

    if(!user){return null}

    async function handleSave({username, email}) {
        await editUser(user.id,username, email, user.roleId);
        setUser(current => ({ ...current, username, email }));
    }
    async function handleDelete() {
        if (!window.confirm("Möchtest du deinen Account dauerhaft löschen?")) {
            return;
        }
        await deleteUser(user.id);
        localStorage.removeItem("accessToken");
        setUser(null)
    }

    return (
        <div className="profile">
            <h1>Mein Profil</h1>
            <h2 className="profile-card-title">Accountdaten</h2>

            <dl className="profile-card profile-details">
                <div>
                    <dt>Benutzername</dt>
                    <dd>{user.username || "Nicht hinterlegt"}</dd>
                </div>
                <div>
                    <dt>E-Mail Adresse</dt>
                    <dd>{user.email}</dd>
                </div>
                <div>
                    <dt>Rolle</dt>
                    <dd>{user.role}</dd>
                </div>
                <div>
                    <dt>User ID</dt>
                    <dd>{user.id}</dd>
                </div>
            </dl>
            <h2 className="profile-card-title">Statistiken</h2>
                {/*Aufrufen der User Statistiken per User ID*/}
                <section className="profile-card">
                    <ProfileStats userId={user.id}/>
                </section>

            {showEditForm && (
                <EditProfileDialog
                    username={user.username}
                    email={user.email}
                    onSave={handleSave}
                    onClose={() => setShowEditForm(false)}
                    onDelete={handleDelete}
                />
            )}
            {/* Button zum Thread anlegen Dialog öffnen */}
            <FloatingActionButton onClick={() => setShowEditForm(true)} content="✏️" />
        </div>
    );
}

export const ProfileSection = {
    title: "Profil",
    icon: "🥸",
    url: "/profile",
    subUrls: [
        /*{
        url: "...",
        element: <... />
        }*/
    ],
    showInSidebar: true,
    element: <Element />
};

export default ProfileSection;
