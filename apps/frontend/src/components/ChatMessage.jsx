export default function ChatMessage({ answer }) {
  if (!answer) return null;

  return (
    <div className="mt-10 w-full max-w-4xl rounded-2xl bg-white p-8 shadow">

      <h2 className="mb-4 text-xl font-bold text-blue-700">
        ⚖️ LexAI
      </h2>

      <p className="whitespace-pre-wrap text-slate-700">
        {answer}
      </p>

    </div>
  );
}