import { useEffect, useRef } from "react";
import "./EditProfileDialog.css";

// Widerverwendbarer modaler Dialog für das Bearbeiten eines Benutzers
export default function EditProfileDialog({username, email, onSave, onClose, onDelete}) {
    const dialogRef = useRef(null);

    useEffect(() => {
        const dialog = dialogRef.current;
        dialog.showModal();
    }, []);

    // Callback wenn abgeschickt wird
    async function handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        try {
            await onSave({
                username: formData.get("username"),
                email: formData.get("email"),
            });
            dialogRef.current?.close();
        } catch(error) {
            console.error(error);
        }
    }
    async function handleDelete() {
        try {
            await onDelete();
            dialogRef.current?.close();
        } catch (error){
            console.error(error);
        }
    }

    return (
        <dialog ref={dialogRef} className="edit-profile-dialog" aria-label="Profil bearbeiten" onClose={onClose}>
            <form onSubmit={handleSubmit}>
                <h2>Profil bearbeiten</h2>
                <label>
                    Username
                    <input name="username" defaultValue={username ?? ""}maxLength={255} required autoFocus placeholder={username}/>
                </label>
                <label>
                    Email Adresse
                    <input name="email" defaultValue={email ?? ""}maxLength={255} required autoFocus placeholder={email}/>
                </label>
                <div className="edit-profile-dialog-actions">
                    <button type="button" className="delete-button" onClick={() => handleDelete()}>Account Löschen</button>
                    <button type="button" onClick={() => dialogRef.current.close()}>Abbrechen</button>
                    <button type="submit">Profil überarbeiten</button>
                </div>
            </form>
        </dialog>
    );
}