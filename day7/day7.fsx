
let compare (a, _) (b, _) =
    let rank a =
        let counts = a
                    |> Seq.countBy(id)
                    |> Seq.sortByDescending(fun (a, b) -> b)
                    |> Seq.map(fun (_, b) -> b)
                    |> Seq.toArray

        match counts with
        | [|5|] -> 7
        | [|4; 1|]-> 6
        | [|3; 2|] -> 5
        | [|3; 1; 1|] -> 4
        | [|2; 2; 1|] -> 3
        | [|2; 1; 1; 1|] -> 2
        | _ -> 1

    let relorder (ch1: char) (ch2: char) =
        let str = "23456789TJQKA"
        str.IndexOf(ch1) - str.IndexOf(ch2)

    let r1 = rank a
    let r2 = rank b
    if r1 - r2 <> 0 then r1 - r2
    else Seq.compareWith relorder a b

let data = System.IO.File.ReadLines "./input1.txt"
        |> Seq.map(fun s -> s.Split())
        |> Seq.map(fun a -> (a.[0], a.[1] |> int))
        |> Seq.sortWith compare
        |> Seq.mapi(fun idx (_, b) -> (idx + 1) * b)
        |> Seq.sum

printfn "Solution 1: %A" data

