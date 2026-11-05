import "./FloatingActionButton.css";

export default function FloatingActionButton({onClick, content}) {
    return (
        <button className="floating-action-button" onClick={onClick} aria-label="">
            <span>{content}</span>
        </button>
    );
}