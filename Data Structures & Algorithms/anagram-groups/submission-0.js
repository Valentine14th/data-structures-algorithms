class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagrams = new Map()
        let acode = 'a'.charCodeAt(0)
        for (const str of strs){
            let letters = Array(26).fill(0)
            for(const c of str){
                if(letters[c.charCodeAt(0) - acode]){
                    letters[c.charCodeAt(0) - acode]++
                }
                else{
                    letters[c.charCodeAt(0) - acode] = 1
                }
            }
            let key = letters.join(',')
            if(anagrams.get(key)){
                anagrams.set(key, anagrams.get(key).concat(str))
            }
            else{
                anagrams.set(key, [str])
            }
        }
        let output = []
        for (const ana of anagrams.values()){
            output.push(ana)
        }
        return output

    }
}
