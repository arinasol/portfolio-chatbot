import Sidebar from "../components/Sidebar";

function Home() {
  return (
    <div className="layout">
      <Sidebar />

      <div className="content">
        Content area
      </div>
    </div>
  );
}

export default Home;