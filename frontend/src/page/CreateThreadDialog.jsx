import { useEffect, useRef, useState } from "react";
import "./CreateThreadDialog.css";

export default function CreateThreadDialog({ groups, onCreate, onClose }) {
    const dialogRef = useRef(null);
    const [saving, setSaving] = useState(false);
    const [error, setError] = useState("");

    useEffect(() => {
        const dialog = dialogRef.current;
        dialog.showModal();
    }, []);

    async function handleSubmit(event) {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        setSaving(true);
        setError("");
        try {
            await onCreate({
                title: formData.get("title"),
                content: formData.get("content"),
                groupId: Number(formData.get("groupId")),
            });
            dialogRef.current?.close();
        } catch {
            setError("Der Beitrag konnte nicht gespeichert werden.");
        } finally {
            setSaving(false);
        }
    }

    return (
        <dialog ref={dialogRef} className="create-thread-dialog" aria-label="Neuer Beitrag" onClose={onClose}
            onCancel={(event) => {
                if (saving)
                    event.preventDefault();
            }}
        >
            <form onSubmit={handleSubmit}>
                <h2>Neuer Beitrag</h2>
                <label>
                    Gruppe
                    <select name="groupId" required>
                        {groups.length === 0 && <option value="">Keine Gruppen verfügbar</option>}
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
                {error && <p role="alert">{error}</p>}
                <div className="create-thread-dialog-actions">
                    <button type="button" disabled={saving} onClick={() => dialogRef.current.close()}>Abbrechen</button>
                    <button type="submit" disabled={saving || groups.length === 0}>
                        {saving ? "Wird gespeichert..." : "Beitrag erstellen"}
                    </button>
                </div>
            </form>
        </dialog>
    );
}
