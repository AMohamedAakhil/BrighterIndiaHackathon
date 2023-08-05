"use client"
import RenderDetails from "@/components/renderDetails"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {useState} from 'react';
import ProgressBar from "@/components/progressbar";

export default function Home() {
  const [search, setSearch] = useState("https://www.youtube.com/watch?v=VLnbuOPL1E4");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    setLoading(true);
  
    try {
      const response = await fetch(`http://127.0.0.1:8000/get_sub?link=${search}`, {cache: 'no-cache'});
  
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      console.log(response);
      const reader = response.body!.getReader();
      const decoder = new TextDecoder();
  
      let data = '';
      let chunk;
  
      while (!(chunk = await reader.read()).done) {
        const chunkText = decoder.decode(chunk.value);
        data += chunkText;
      }
  
      const parsedData = JSON.parse(data);
      console.log(parsedData);
  
      setData(parsedData); // Assuming you have a `setData` function to set the data state
      console.log(parsedData);
  
    } catch (error) {
      console.error("Error fetching data:", error);
      // Handle the error appropriately in your React app.
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <main className="bg-slate-950">
      <div className="bg-black w-full p-5 text-white">
        <h1 className="text-white font-bold">
        Brighter India Hackathon
        </h1>

      </div>
    <div className="p-6 w-full">
      <h1 className="text-2xl text-white">Reel Generator</h1>
      <form className="w-full">

      <div className="flex w-full items-center space-x-2 mt-5">
        <Input onChange={(e) => (setSearch(e.target.value))} type="text" className="w-full" placeholder="URL" />
        <Button onClick={(e) => handleSubmit(e)} className="w-1/8" type="submit">Search</Button>
    </div>
    </form>
    <h1>{loading ? <div className="mt-7 w-full"><ProgressBar  /></div> : <RenderDetails choices={data} search={search} /> }
    </h1>
    </div>
    </main>
  )
}
