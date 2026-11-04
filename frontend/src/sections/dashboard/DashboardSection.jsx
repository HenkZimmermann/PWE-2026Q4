import FloatingActionButton from "../../page/FloatingActionButton";

function Element() {
    const handleCreate = () => {
        alert("Neu"); // TODO, beispiel alert
    };

    return (
        <div>
            <h1>Dashboard</h1>
            <FloatingActionButton onClick={handleCreate} content="+" />
        </div>
    );
}
export const DashboardSection = {
    title: "Dashboard",
    icon: "🖥️",
    url: "/",
    subUrls: [
        /*{
        url: "...",
        element: <... />
        }*/
    ],
    showInSidebar: true,
    element: <Element />,
};

export default DashboardSection;