import { useEffect, useRef } from "react";
import "./CreateThreadDialog.css";

// Widerverwendbarer modaler Dialog für das Erstellen von einem Thread
export default function CreateThreadDialog({groups, onCreate, onClose}) {
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
            await onCreate({
                title: formData.get("title"),
                content: formData.get("content"),
                groupId: Number(formData.get("groupId")),
            });
            dialogRef.current?.close();
        } catch {
            console.error(error);
        }
    }

    return (
        <dialog ref={dialogRef} className="create-thread-dialog" aria-label="Neuer Beitrag" onClose={onClose}>
            <form onSubmit={handleSubmit}>
                <h2>Neuer Beitrag</h2>
                <label>
                    Gruppe
                    <select name="groupId" required>
                        {groups.map((group) => <option key={group.id} value={group.id}>{group.name}</option>)}
                    </select>
                </label>
                <label>
                    Titel
                    <input name="title" maxLength={255} required autoFocus />
                </label>
                <label>
                    Text
                    <textarea name="content" rows={4} required />
                </label>
                <div className="create-thread-dialog-actions">
                    <button type="button" onClick={() => dialogRef.current.close()}>Abbrechen</button>
                    <button type="submit">Beitrag erstellen</button>
                </div>
            </form>
        </dialog>
    );
}
