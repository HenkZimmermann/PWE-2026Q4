import { useState } from "react";
import "./VoteControls.css";

export default function VoteControls({label}) {
    const [vote, setVote] = useState(0);

    function toggleVote(direction) {
        setVote((current) => current === direction ? 0 : direction);
    }

    return (
        <div className="vote-controls" role="group" aria-label={label}>
            <button type="button" aria-label="Upvote" aria-pressed={vote === 1} onClick={() => toggleVote(1)}>
                ↑
            </button>
            <output aria-label="Votes">{vote}</output>
            <button type="button" aria-label="Downvote" aria-pressed={vote === -1} onClick={() => toggleVote(-1)}>
                ↓
            </button>
        </div>
    );
}
