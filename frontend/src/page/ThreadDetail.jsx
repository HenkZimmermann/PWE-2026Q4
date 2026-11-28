import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { deleteThread, editThread, getThreadById } from "../api/threads";
import { useUser } from "../context/UserProvider";
import EditThreadDialog from "./EditThreadDialog";
import ThreadCard from "./ThreadCard";
import ThreadComments from "./ThreadComments";
import "./ThreadDetail.css";

export default function ThreadDetail() {
    const {threadId} = useParams();
    const navigate = useNavigate();
    const {user} = useUser();
    const [thread, setThread] = useState(null);
    const [editing, setEditing] = useState(false);

    useEffect(() => {
        let active = true;
        setThread(null);
        setEditing(false);

        getThreadById(threadId)
            .then((thread) => {
                if (active)
                    setThread(thread);
            })
            .catch((error) => console.error(error));

        return () => {
            active = false;
        };
    }, [threadId]);

    function handleCommentCreated(commentThreadId) {
        setThread((current) => current?.id === commentThreadId
            ? {...current, commentCount: current.commentCount + 1}
            : current);
    }

    async function handleEdit(changes) {
        const id = thread.id;
        await editThread(id, changes);
        setThread((current) => current?.id === id ? {...current, ...changes} : current);
    }

    async function handleDelete() {
        if (!window.confirm("Diesen Beitrag und alle Kommentare endgültig löschen?"))
            return;

        try {
            await deleteThread(thread.id);
            // Thread gelöscht also zurück auf standard Ansicht
            navigate("/", {replace: true});
        } catch (error) {
            console.error(error);
        }
    }

    const canManage = user && thread && (user.id === thread.authorId || user.role === "Admin");

    return (
        <div className="thread-detail">
            {thread === null ? (
                <p role="status">Beitrag nicht gefunden.</p>
            ) : (
                <>
                    <ThreadCard thread={thread} onEdit={canManage ? () => setEditing(true) : undefined} onDelete={canManage ? handleDelete : undefined} />
                    {editing && <EditThreadDialog thread={thread} onSave={handleEdit} onClose={() => setEditing(false)} />}
                    <ThreadComments key={thread.id} threadId={thread.id} onCommentCreated={handleCommentCreated} />
                </>
            )}
        </div>
    );
}
