export default function Navbar() {
  return (
    <nav className="w-full border-b bg-white">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-8 py-5">
        <h1 className="text-2xl font-bold text-blue-800">
          ⚖️ LexAI
        </h1>

        <button className="rounded-lg border px-4 py-2 transition hover:bg-slate-100">
          About
        </button>
      </div>
    </nav>
  );
}