function permute(nums: number[]): number[][] {
    let res: number[][] = []
    const backtrack = (cur: number[], rem: number[]) => {
        if (!rem.length) {
            res.push(cur)
            return
        }
        for (var num of rem) {
            backtrack([...cur, num], rem.filter((n) => n != num))
        }
    }
    backtrack([], nums)
    return res
};

// same as 46v1