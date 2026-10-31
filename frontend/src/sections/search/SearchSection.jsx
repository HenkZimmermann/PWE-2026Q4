function Element() {
    return (<h1>Suche</h1>);
}

export const SearchSection = {
    title: "Search",
    icon: "🔎",
    url: "/search",
    subUrls: [
        /*{
        url: "...",
        element: <... />
        }*/
    ],
    showInSidebar: true,
    element: <Element />,
};

export default SearchSection;