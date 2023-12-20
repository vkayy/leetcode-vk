async function sleep(millis: number): Promise<void> {
  await new Promise(resolve => setTimeout(resolve, millis))
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

// we return a promise that resolves after the given time
// we use setTimeout to resolve the promise after the given time
