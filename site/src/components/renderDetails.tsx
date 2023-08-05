"use client"
import React from 'react'
import ReactPlayer from 'react-player'


const RenderDetails =  ({choices, search}: any) => {
  console.log(choices); 
  const formattedChoices = choices ? choices.replace(/\n/g, '<br />') : "Rate limit exceeded. Try again later.";

  
  return (
    <div className="mt-10 text-white w-full flex flex-row justify-between">
      <div className="w-full">
        <h1 className="text-2xl text-white mb-4">Transcript :</h1>
        <h1 dangerouslySetInnerHTML={{ __html: formattedChoices }} />
      </div>
      <div className='w-full'>{
        choices ? 
      
        <video autoPlay controls src={('C:/Users/Aakhil/Desktop/BrighterIndiaHackathon/model/downloadsnew_vid.mp4')} /> : null }
        <ReactPlayer url={search} controls={true} />
      </div>
      
    </div>
  )
}

export default RenderDetails