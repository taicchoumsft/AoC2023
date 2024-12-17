type Lens = {key: int; value: int}

let data = System.IO.File.ReadLines "./input1.txt"
        |> Seq.collect _.Split([|','|])

let hash (a: string) = a |> Seq.fold (fun acc ch -> ((acc + (int) ch) * 17) % 256) 0

printfn "Solution 1: %A" (data |> Seq.sumBy hash)

let addOrReplace (lens: List<string * int>) (l: string * int) =
    let k = (fst l)
    let v = (snd l)

    let rec inner arr =
        match arr with
        | [] -> [l]
        | (k', v') :: xs when k = k' -> (k, v) :: xs
        | x :: xs -> x :: (inner xs)

    inner lens

let sol2 =
    data
    |> Seq.fold (fun (acc: List<string * int>[]) op ->
        let [| opName;  lenVal|] = op.Split([|','|], 2)
        let k = hash opName
        let v = lenVal |> int

        let box = acc.[k]
        let newBox = addOrReplace box (opName, v)
        Array.set acc k newBox
        acc
    ) (Array.zeroCreate 256)

printfn "%A" sol2
