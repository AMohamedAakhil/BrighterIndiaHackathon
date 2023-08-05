"use client"
import React from 'react'

const RenderDetails =  (data: any) => {
  console.log(data);
  
  return (
    <div className="mt-5">
      {data.choices[0].message}
    </div>
  )
}

export default RenderDetails