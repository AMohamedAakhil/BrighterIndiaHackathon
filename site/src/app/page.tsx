"use client"
import RenderDetails from "@/components/renderDetails"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import {useState} from 'react';

async function fetchData(link: string) {

  const res = await fetch(`http://127.0.0.1:8000/get_sub/?link=${link}`)
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
    <div className=" w-full bg-black p-6 text-white">Brighter India Hackathon</div>
    <div className="p-6">
      <h1 className="text-2xl">Reel Generator</h1>
      <div className="flex w-full max-w-sm items-center space-x-2 mt-5">
        <form>
        <Input onChange={(e) => (setSearch(e.target.value))} type="text" placeholder="URL" />
        <Button onClick={(e) => handleSubmit(e)} type="submit">Search</Button>
    </form>
 
    </div>
    </div>
    </main>
  )
}
