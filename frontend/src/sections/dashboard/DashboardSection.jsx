function Element() {
    return (<h1>Dashboard</h1>);
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