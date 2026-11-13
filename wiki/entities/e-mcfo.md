---
title: 多色隨機單細胞標記（MultiColor FlpOut, MCFO）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# 多色隨機單細胞標記（MultiColor FlpOut, MCFO）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **驅動品系、split-GAL4**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。一個品系常常同時標到好幾顆細胞，螢光糊成一團，分不出單顆的形狀。
- **flip-out**：用 FLP 重組酶隨機切掉一段「阻擋」序列，只有被切到的少數細胞才表現標記，於是看得到單顆細胞的完整形態。
- **細胞型（cell type）**：形態與連結相同的一群細胞，一型可以只有一顆，也可以有好幾顆。
- **雙色標記**：用 GAL4 與 LexA 兩套互不干擾的系統，各標一型細胞、各用一種顏色。
- **蕈狀體（mushroom body）、MBON、DAN、KC**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）；其中的輸出神經元、多巴胺神經元、代表氣味的 Kenyon 細胞。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認。

## 是什麼

**MCFO 讓一個驅動品系標到的細胞裡，隨機只有少數幾顆各自帶上不同顏色的標籤，用來在一團螢光中分出單顆細胞的形狀。** Aso 2014a 的說法是隨機讓少數細胞各帶一種抗原標籤、顯成不同顏色；Ichinose 2015 與 Aso 2023 都用它回答「這一型有幾顆、每顆長什麼樣」。它是光學顯微鏡的方法，看得到形態與重疊，看不到突觸。Mao 2009 用的是較早的單色 flip-out 單細胞選殖（熱休克誘發，一次只看一顆綠色細胞），不是 MCFO，本頁不列。

## 版本與規模（庫內各篇的用量）

| 來源 | 品系 | 規模 |
|---|---|---|
| Aso 2014a | 92 個 split-GAL4 最佳品系中的多個（例如 MB077B、MB469B、MB371B、MB060B） | 未給總腦數 |
| Aso 2023 | SS33917 | 37 顆腦 → 25 張單細胞影像 |
| Ichinose 2015 | 未在來源頁寫明（MBON-α1 的品系為 MB310C） | 一張圖（圖 1G） |

各篇用的 MCFO 試劑版本，來源頁都沒有記錄：？待查。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 本篇定義「細胞型」的操作工具：MCFO 拆不開的同品系細胞算同型，拆得開的算不同型；也用來拆出單顆 KC 的分枝樣式（圖 6、7）、驗證區室交界（圖 11） | 例：MB077B 的兩顆 MBON-γ2α′1 拆不開，屬同型（圖 8B）；以雙色標記或 MCFO 檢驗的 11 個區室交界全部確認，第 12 個（β1／β2）因缺品系未測；單腦 MCFO 的三型 PPL1 DAN 位置，被用作影像對位品質的同腦對照（圖 11F、22G） |
| [[s-aso-2014-mbon-valence]] | 單細胞標記，配合雙色標記看 MBON-γ1pedc>α/β 與 PPL1-γ1pedc 的位置 | 兩者在 γ1 與 pedc 精確重疊（圖 6K） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 把 MBON-α1 的個別細胞標成紅與青 | MBON-α1 是兩顆形態很相似的細胞，末梢都伸到 SIP 與 SLP（圖 1G；見 [[numbers]]） |
| [[s-aso-2023-upwind-neurons]] | SS33917 的單細胞影像拿去比對 [[e-hemibrain]] 的電顯神經元 | 對到 11 顆、5 型的 UpWiN（迎風神經元） |
| [[s-yamada-2023-second-order-conditioning]] | 以 SS67221 做多色 flip-out，看 SMP108 單顆形態 | SMP108 是左右各一顆，軸突各自跨到對側（圖 4F） |

## 已知的問題

- **「同型」是操作型定義。** Aso 2014a 的「拆不開＝同型」取決於所用的 7000 個 GAL4 品系；換更細的工具（例如電顯）可能再分出型（※ 推論，依定義本身推得）。
- **單細胞像的數目不等於細胞數。** Aso 2023 的 37 顆腦得 25 張單細胞像、對到 11 顆電顯神經元——是「形態比對」，每顆電顯神經元是否都有 MCFO 對應影像，來源頁沒有逐顆列出：？待查。
- **沒做 MCFO 就是品系涵蓋範圍的弱點。** Burke 2012 判定品系涵蓋範圍只靠引用與群體影像，沒有做單細胞解析度的驗證（該來源頁的評語，本頁不列為使用者）；庫內品系涵蓋範圍的爭議見 [[syn-contradictions]] 1.4、1.5。
- **重疊不等於相連。** Aso 2014b 圖 6K 與 Aso 2014a 都只能說兩型細胞落在同一格，突觸要靠電顯或 [[e-grasp]] 之類的方法再檢驗。

## 相關

- 品系：[[e-split-gal4]]；接續的比對對象：[[e-hemibrain]]
- 細胞：[[e-mbon-alpha1]]、[[e-mbon-gamma1pedc]]、[[e-ppl1-gamma1pedc]]、[[e-kenyon-cell]]
- 概念：[[c-mb-compartment]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]
- 待開頁面：`c-flp-out-clone`、`e-pa-gfp`、`e-mb077b`、`e-mb060b`、`e-mb310c`
