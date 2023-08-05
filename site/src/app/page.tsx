"use client"
import RenderDetails from "@/components/renderDetails"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {useState} from 'react';

async function fetchData(link: string) {

  const res = await fetch(`https://jsonplaceholder.typicode.com/todos/1`)
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
 
  return res.json()
}

export default function Home() {
  const [search, setSearch] = useState("");
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const data = await fetchData(search)
    console.log(data);
  }
  return (
    <main>
      <div className="bg-black w-full p-5 text-white">
        <h1>
        Brighter India Hackathon
        </h1>

      </div>
    <div className="p-6">
      <h1 className="text-2xl">Reel Generator</h1>
      <form>

      <div className="flex w-full max-w-sm items-center space-x-2 mt-5">
        <Input onChange={(e) => (setSearch(e.target.value))} type="text" placeholder="URL" />
        <Button onClick={(e) => handleSubmit(e)} type="submit">Search</Button>
    </div>
    </form>

    </div>
    </main>
  )
}
