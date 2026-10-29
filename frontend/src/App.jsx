import Sections from './sections/Sections'

function App() {
    return (
        <div>
            {Sections.map((section) => (
                section.element
            ))}
        </div>
    );
}

export default App;