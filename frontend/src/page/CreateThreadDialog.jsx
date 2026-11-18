import { useEffect, useRef } from "react";
import "./CreateThreadDialog.css";

export default function CreateThreadDialog({ groups, onCreate, onClose }) {
    const dialogRef = useRef(null);

    useEffect(() => {
        const dialog = dialogRef.current;
        dialog.showModal();
    }, []);

    function handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        onCreate({
            title: formData.get("title"),
            content: formData.get("content"),
            groupName: formData.get("groupName"),
        });
        dialogRef.current.close();
    }

    return (
        <dialog ref={dialogRef} className="create-thread-dialog" aria-label="Neuer Beitrag" onClose={onClose}>
            <form onSubmit={handleSubmit}>
                <h2>Neuer Beitrag</h2>
                <label>
                    Gruppe
                    <select name="groupName" required>
                        {groups.map((group) => <option key={group}>{group}</option>)}
                    </select>
                </label>
                <label>
                    Titel
                    <input name="title" required autoFocus />
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
