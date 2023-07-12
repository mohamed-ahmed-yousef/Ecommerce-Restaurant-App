export function capitalize(element) {
  if(typeof element !== "string") return element // return if the passed value is object. i will make the object uppercase by my hand.

  
    const ans = element.split(" ").map(ele => {
      return (
        ele.charAt(0).toUpperCase()+ele.slice(1,)
      )
    }).join(" ")
    return ans
  }
