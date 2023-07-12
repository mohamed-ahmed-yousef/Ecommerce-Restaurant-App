export function capitalize(element) {
    const ans = element.split(" ").map(ele => {
      return (
        ele.charAt(0).toUpperCase()+ele.slice(1,)
      )
    }).join(" ")
    console.log(ans);
    return ans
  }

export function Minize(element) {
    const ans = element.split(" ").map(ele => {
        return (
          ele.charAt(0).toLowerCase()+ele.slice(1,)
        )
      }).join(" ")
      console.log(ans);
      return ans
    }

