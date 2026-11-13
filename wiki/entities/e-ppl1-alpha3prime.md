---
title: PPL1-α′3 多巴胺神經元（PPL1-α′3）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: low
---

# PPL1-α′3 多巴胺神經元（PPL1-α′3）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，往上的垂直葉有 α 與 α′ 兩條，每條葉沿長度切成一格一格的「區室」；α′3 在 α′ 葉的尖端，α3 在 α 葉的尖端，兩格相鄰但屬於不同的葉。細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PPL1 是細胞體在腦後外側的一群，多傳遞懲罰（見 [[e-dopaminergic-neuron]]）。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、把結果送出蕈狀體（見 [[e-mbon]]）。
- **CS+／CS−**：訓練時配了電擊或糖的氣味（CS+），與沒配的對照氣味（CS−）。
- **消退**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱（[[c-memory-extinction]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）；TH-GAL4 標到大部分多巴胺神經元（[[e-th-gal4]]）。flip-out 選殖＝在廣泛品系裡隨機只讓一顆細胞發光，用來看單顆細胞的形狀。
- **讀數**：ΔF/F＝螢光相對刺激前的變化比例，以遇鈣變亮的 G-CaMP 量神經元活動（[[e-gcamp]]），看不太出活動「減少」；Post/Pre＝處理後反應佔處理前的百分比。電壓成像＝用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電與放電減少。shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]）。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「該頁」指表格同一列的來源頁。

## 是什麼

**PPL1-α′3 是 PPL1 群中的一型多巴胺神經元，把多巴胺送進蕈狀體 α′ 葉尖端的 α′3 區室。** 它與 [[e-ppl1-alpha3]]（送進 α 葉尖端的 α3）是兩型不同的細胞：Mao 2009 的單細胞選殖顯示，支配 α 尖端的那顆細胞不進入緊鄰的 α′ 尖端（圖 5B2）。依 Aso 2014a 表 1，支配蕈狀體的 PPL1 有六型（γ1pedc、γ1、γ2α′1、α′3、α′2α2、α3），除 γ1pedc 為 1–2 顆外每型 1 顆；Huang 2024 量的五型 PPL1 也包含它。同一格的輸出神經元是 MBON-α′3ap 與 MBON-α′3m（Aso 2014a 圖 16D），不是 [[e-mbon-alpha3]]。在本庫，它的特徵是**對電擊反應弱、對氣味反應強**，以及在已收的訓練實驗裡沒有看到它改變。

## 版本與規模（標記它的品系）

| 品系 | 來源 | 說明 |
|---|---|---|
| MB308B（split-GAL4） | Felsenberg 2017 延伸圖 3e、6h | 延伸圖 6h 說它標 PPL1-α′3、在 α3 只有弱表現；但該篇正文把被阻斷的一型寫成「PPL1-α3」 |
| MB099C（split-GAL4） | Hige 2015 | Hige 2015 說它標四型 PPL1，含 α′3；Aso 2016 說只有兩型、不含 α′3（[[syn-contradictions]] 1.4，見 [[e-mb099c]]） |
| TH-GAL4 | Mao 2009；Felsenberg 2017 延伸圖 6b | 群體品系，標到包含它在內的六型 PPL1 |

Huang 2024 以哪一條品系量它，來源頁沒有列出（？待查）。

## 庫內誰用了它

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-mao-2009-dopaminergic-neuron-types]] | TH-GAL4 flip-out 單細胞選殖；TH-GAL4 > G-CaMP 群體鈣成像，量 α′ 尖端的多巴胺末梢 | 選殖中支配 α′ 尖端的 PPL1 一型（5 個樣本）。0.01 mA 電擊約 8%（n＝6）、0.1% MCH 約 38%（n＝31），對氣味遠強於電擊，與 α 尖端相反（約 48% 與 13%）。1 分鐘處理後 10 分鐘的 Post/Pre：未處理 117%、順向 56%、逆向 51%、只氣味 72%、只電擊 148%，沒有專屬於配對的改變（皆 ※ 從圖判讀）。「α′ 尖端＝PPL1-α′3」是該頁依位置的 ※ 推論 |
| [[s-aso-2014-mb-architecture]] | split-GAL4 解剖分類 | 列為六型 PPL1 之一、1 顆；圖 16E 有它的影像 |
| [[s-felsenberg-2017-re-evaluation]] | MB308B 驅動 shi，在糖獎賞記憶再聞 CS+ 時阻斷 | 消退不受影響（延伸圖 3e） |
| [[s-huang-2024-dopamine-memory-dynamics]] | 頭固定、腳踩小球的活果蠅上以電壓成像量放電 | 自發約 9 次／s，五型 PPL1 中最低（※ 從圖判讀）；單下電擊與吃糖都無顯著變化；其他四型的氣味反應與果蠅的好惡呈負相關，它不論氣味好惡主要是上升；6 回合電擊訓練後對 CS+、CS− 都不變。沒有放進模型 |

數值見各來源頁與 [[numbers]]。Aso 2019 只在註記中提到 PPL1 不只四型（引 Huang 2024 的五型含 α′3），沒有操作它，不列入表。

## 已知的問題

- **Mao 2009 的對應是推論。** 該篇沒有給 α′ 尖端這一型命名；「就是 PPL1-α′3」是 Mao 來源頁依位置推得。群體品系的訊號也可能混有鄰近段或其他細胞。兩篇一致的是「對電擊弱」的排序（Mao 的 α′ 尖端約 8%；Huang 的 α′3 不顯著），不是數值。
- **只聞氣味後反應會不會下降，兩篇看法不同。** Mao 2009 的 α′ 尖端在只氣味組約 72%（未標顯著）；Huang 2024 說 CS− 引起的反應在所有 PPL1 都不變。讀數、氣味、協定都不同（見 [[syn-contradictions]] 1.11）。
- **Felsenberg 2017 的命名自身不一致。** 正文寫「PPL1-α3」、延伸圖 3e 圖說寫「PPL1-α3 與 PPL1-α′3」、延伸圖 6h 說 MB308B 主要標 α′3（⚠️ 單篇自身不一致）。依延伸圖 6h，該篇的陰性結果較可能是關於本型而非 PPL1-α3（※ 推論）。
- **Huang 2024 的型名前後不一。** 正文寫 PPL1-α′3m，圖 1–3 寫 PPL1-α′3（⚠️ 單篇自身不一致）。
- **它在學習裡做什麼，本庫沒有正面資料。** 庫內唯一的阻斷是陰性（Felsenberg 2017），成像都沒看到訓練造成的改變；沒有來源單獨活化它。

## 相關

- 相鄰而不同的一型：[[e-ppl1-alpha3]]；同群其他型：[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-ppl1-alpha2alpha2]]；細胞群：[[e-dopaminergic-neuron]]
- 品系與工具：[[e-th-gal4]]、[[e-mb099c]]、[[e-split-gal4]]、[[e-shibire-ts]]、[[e-gcamp]]
- 概念：[[c-mb-compartment]]、[[c-memory-extinction]]、[[c-valence-coding]]
- 主題：[[t-memory-updating]]、[[t-innate-learned-integration]]；矛盾：[[syn-contradictions]]
- 來源：[[s-mao-2009-dopaminergic-neuron-types]]、[[s-aso-2014-mb-architecture]]、[[s-felsenberg-2017-re-evaluation]]、[[s-huang-2024-dopamine-memory-dynamics]]
- 待開頁面：`e-mb308b`、`e-mbon-alpha3prime`
