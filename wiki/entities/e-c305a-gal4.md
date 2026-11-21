---
title: c305a-GAL4 驅動品系（c305a-GAL4）
created: 2026-11-13
updated: 2026-11-21
tags: [entity, active, cross-domain]
confidence: medium
---

# c305a-GAL4 驅動品系（c305a-GAL4）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **驅動品系（driver line）**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。
- **蕈狀體（mushroom body）、KC、葉、柄**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）。代表氣味的 Kenyon 細胞（KC，[[e-kenyon-cell]]）的樹突在萼部（calyx）收嗅覺輸入，軸突束成「柄」（pedunculus）往前，再分岔成往上的垂直葉與往內的水平葉。KC 分三類：α/β、α′/β′、γ；**α′/β′ KC 的軸突分岔成 α′ 葉（垂直）與 β′ 葉（水平）**（依 [[s-tomchik-2009-camp-dynamics]] 的說明）。
- **區室（compartment）**：葉沿長度切成的一格一格，例如 β′2、α′3；細胞以所在區室命名（[[c-mb-compartment]]）。
- **DAN、抗 TH 染色**：送出獎賞或懲罰訊號的多巴胺神經元；抗 TH 抗體染出製造多巴胺所需的酵素，用來看多巴胺細胞在哪裡。
- **cAMP、Epac1-camps**：細胞內的訊息分子；Epac1-camps 是量 cAMP 的螢光感測器（[[e-epac-camp-sensor]]）。
- **LI（學習指數）**：行為分數，一群果蠅在兩種氣味間選擇換算成一個數（[[c-performance-index]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**c305a-GAL4 是庫內各篇用來取用 α′/β′ 型 Kenyon 細胞的 GAL4 驅動品系。** 庫內四篇用它（[[s-vogt-2014-shared-visual-olfactory-circuits]] 的用法見下表）：[[s-kaldun-2025-dop1r2-memory-phases]] 用它只在這群細胞切除多巴胺受體，[[s-tomchik-2009-camp-dynamics]] 用它把 cAMP 感測器送進這群細胞的軸突，[[s-mao-2009-dopaminergic-neuron-types]] 只拿它當「這裡是 β′ 葉」「這裡是柄的末端」的解剖地標。它是一般的 GAL4，不是 split-GAL4。來源編號只有 Kaldun 2025 寫出：Bloomington BL 30829。

**各篇對它標到什麼的寫法寬窄不同：**Kaldun 2025、Tomchik 2009 與 Vogt 2014 寫 α′/β′，Mao 2009 寫 β′ 葉。※ 推論：Mao 2009 那兩張圖看的是水平葉與柄，用得到的只有 α′/β′ KC 的水平那一支（β′ 葉）與軸突經過的柄，所以寬窄不同反映的是圖上用到的範圍，不一定是對品系標記範圍的不同主張；三篇都沒有逐顆清點這個品系標到哪些細胞（？待查），所以本庫不把它登記為矛盾。

## 版本與規模（庫內各篇的用量）


| 來源 | 該頁的寫法 | 搭配的效應基因／感測器 | 同篇的對照品系 |
|---|---|---|---|
| Kaldun 2025 | α′/β′ 葉 | 20×UAS-FLP<sup>G5.PEST</sup>（BL 55807），在 Dop1R2<sup>cko</sup> 背景下切除受體 | OK107（全蕈狀體）、5HTR1B（γ）、c739（α/β），另有 elav（泛神經元） |
| Tomchik 2009 | α′/β′ KC | UAS-epac1-camps（cAMP 感測器） | 238Y（三類 KC）、c739（α/β）、1471（γ）、c316（DPM）、GH146（投射神經元） |
| Mao 2009 | β′ 葉 | UAS-mCD8::GFP（當輪廓地標，與抗 TH 疊圖） | NP1131（γ 葉）、c739（β 葉）、OK107（全部 KC） |
| Vogt 2014 | α′/β′ 神經元（正文與方法寫 c305a-GAL4，**圖 6 的圖說與橫軸寫 c305-GAL4**，⚠️ 單篇書寫不一致） | UAS-shi<sup>ts1</sup>（[[e-shibire-ts]]） | 17D（α/β）、201y（α/β 與 γ）；另有四條 split-GAL4：MB010B、MB009B、[[e-mb008b]]、MB186B |

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-kaldun-2025-dop1r2-memory-phases]] | 只在 α′/β′ KC 切除多巴胺受體 Dop1R2（[[e-dopamine-receptor]]） | 訓練後立刻測不受影響；2 小時記憶嫌惡由三組對照均值約 33.5 降到約 7（21%）、獎賞約 44.8 → 26.5（59%）；24 小時嫌惡約 62.3 → 7.5（12%）、獎賞約 42.8 → 10.5（25%）（皆 ※ 從圖判讀，各組 N＝12；嫌惡 2 小時那一格因非常態改用 Kruskal–Wallis＋Dunn） |
| [[s-tomchik-2009-camp-dynamics]] | 在離體腦量 α′ 葉中 α′/β′ KC 軸突的 cAMP 對多巴胺與章魚胺的劑量反應（圖 4B） | γ 葉（1471）與 α′ 葉（c305a）對多巴胺與章魚胺的敏感度沒有分出高下（p＝0.95、0.38，每組 n＝5），而 α 葉與投射神經元是章魚胺遠較敏感——各類 KC 讀取這兩種傳遞物的方式在 cAMP 層級就不一樣 |
| [[s-vogt-2014-shared-visual-olfactory-circuits]] | 全程阻斷 α′/β′ KC 的輸出，**同時**測嫌惡顏色記憶與嫌惡氣味記憶 | 顏色記憶完全不受影響（−0.141 對 −0.104／−0.102，殘存約 137%）；氣味記憶由 −0.625 升到 −0.152（殘存約 22%，p < 0.001），n = 12–19／10–22。這是庫內唯一一次在同一篇裡把這條品系放在兩種感覺模態上並排測。**兩個作業的基準 LI 差六倍，視覺側的陰性結果偵測力較低**（見該來源頁第五節第 7 條）。本篇沒有做這條品系的氣味感覺對照：？待查 |
| [[s-mao-2009-dopaminergic-neuron-types]] | 標出 β′ 葉與柄末端的輪廓，與抗 TH 染色疊圖（圖 3E、圖 4C） | β′ 葉內側尖端有強烈的多巴胺突起支配（圖 4C3 圖說）；圖 3E 借 c305a 的 KC 軸突描出柄末端的形狀，讓抗 TH 訊號有位置可對（本庫註，※ 推論） |

數值見 [[numbers]]。

## 已知的問題

- **標記範圍沒有被量化。** 四篇都沒有寫它標到幾顆 KC、是否漏標或多標到別的細胞：？待查。Mao 2009 寫 β′、另兩篇寫 α′/β′（見「是什麼」）。
- **剪除效率沒有在這個品系上驗證。** [[s-kaldun-2025-dop1r2-memory-phases]] 的抗 HA 染色只做了 OK107（全蕈狀體）那一組，三個分葉品系（含 c305a）沒有對應的染色，該篇補充圖本庫未取得。所以用 c305a 得到的**陽性**結果可信；同篇 γ 葉的**陰性**結果不能據此推論。
- **「α′/β′ 需要、γ 不需要」沒有被直接檢定。** Kaldun 2025 比較的是各品系各自對自己的三組親代對照，論文沒有對不同品系之間的減損幅度做統計比較。
- **Tomchik 2009 的 c305a 組量的是 α′ 葉，不是 β′ 葉。** 同一群細胞的兩支軸突是否行為相同，該篇沒有檢驗：？待查。
- **Mao 2009 的用法是地標，不是功能實驗。** 引用它時不要寫成「Mao 2009 操弄了 α′/β′ KC」。
- **「α′/β′ 只管嗅覺」這個結論的兩半偵測力不同。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 在同一篇裡並排測兩種模態：氣味側是**陽性**結果（殘存 22%，p < 0.001，對照 LI 約 −0.63），視覺側是**陰性**結果（殘存 137%，對照 LI 約 −0.10）。兩個作業的基準分數差約六倍，所以視覺側的「沒有效果」能排除的效果量比氣味側小得多，而該篇沒有做功效分析。引用這個雙重分離時要寫出這一點。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-mushroom-body]]
- 其他 KC 品系：[[e-c739-gal4]]（α/β）、[[e-238y-gal4]]（三類 KC）、[[e-ok107-gal4]]（全部 KC）；品系原理見 [[e-split-gal4]]
- 工具：[[e-epac-camp-sensor]]、[[e-dopamine-receptor]]、[[e-th-gal4]]
- 概念：[[c-mb-compartment]]、[[c-camp-signaling]]、[[c-memory-consolidation]]、[[c-performance-index]]
- 來源：[[s-kaldun-2025-dop1r2-memory-phases]]、[[s-tomchik-2009-camp-dynamics]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-vogt-2014-shared-visual-olfactory-circuits]]
- 待開頁面：`e-1471-gal4`、`e-5htr1b-gal4`、`e-np1131-gal4`、`c-conditional-knockout`
