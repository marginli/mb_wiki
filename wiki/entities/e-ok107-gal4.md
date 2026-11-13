---
title: OK107-GAL4 驅動品系（OK107-GAL4）
created: 2026-11-13
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# OK107-GAL4 驅動品系（OK107-GAL4）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **驅動品系（driver line）**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半，兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「GAL4>UAS-X」表示由該 GAL4 驅動 X。
- **蕈狀體（mushroom body）、KC、葉、區室**：果蠅腦中把氣味和好壞經驗連起來的構造（[[e-mushroom-body]]）。代表氣味的 Kenyon 細胞（KC，[[e-kenyon-cell]]）把軸突成束排成 α、α′、β、β′、γ 幾條「葉」，每條葉沿長度切成一格一格的「區室」（[[c-mb-compartment]]）。KC 分三類：α/β、α′/β′、γ。
- **DAN、MBON**：送出獎賞或懲罰訊號的多巴胺神經元；讀出 KC 訊號、推動果蠅靠近或走開的蕈狀體輸出神經元。
- **IPCs（insulin-producing cells）**：製造胰島素的細胞，不屬於蕈狀體。
- **感測器**：GCaMP 遇鈣變亮（[[e-gcamp]]）；EPAC 量 cAMP（[[e-epac-camp-sensor]]）；GRAB_DA1m 量細胞外多巴胺；ER-GCaMP6-210 放在內質網腔內，變暗代表內質網放出鈣。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值。

## 是什麼

**OK107-GAL4 是庫內各篇用來代表「全部 Kenyon 細胞」的 GAL4 驅動品系。** 庫內五篇用到它：三篇把它當成把感測器或效應基因送進 KC 的工具（Dylla 2017、Handler 2019、Kaldun 2025），一篇只拿它當「這裡是蕈狀體、是全部的葉」的解剖地標（Mao 2009），一篇在方法的驅動品系清單中列出它、但沒有指明用在哪一個實驗（Pribbenow 2022）。它是一般的 GAL4，不是 split-GAL4。來源編號只有 [[s-kaldun-2025-dop1r2-memory-phases]] 寫出：京都 DGGR_106098。

它標到多少顆 KC、是否涵蓋全部三類 KC，五篇都沒有給數字：？待查。庫內另外三個 KC 驅動品系是 [[e-c739-gal4]]（α/β）、[[e-c305a-gal4]]（α′/β′）、[[e-238y-gal4]]（三類 KC），可與它對照。

## 版本與規模（庫內各篇的用量）

| 來源 | 標到的細胞（該頁寫法） | 搭配的效應基因／感測器 |
|---|---|---|
| Kaldun 2025 | 全蕈狀體 | 20×UAS-FLP<sup>G5.PEST</sup>（BL 55807），在 Dop1R2<sup>cko</sup> 背景下切除多巴胺受體 |
| Dylla 2017 | 全部 KC | UAS-GCaMP3（子代稱 OK107>GCaMP3） |
| Handler 2019 | KC 軸突 | EPAC（cAMP，FRET）、ER-GCaMP6-210（內質網鈣）、GRAB_DA1m（多巴胺） |
| Pribbenow 2022 | KC | 該頁只在驅動品系清單中列出，未寫搭配哪一個效應基因：？待查 |
| Mao 2009 | 全部 KC | UAS-mCD8::GFP（當作「哪一葉」的地標，與抗 TH 疊圖） |

## 庫內誰用了它

| 來源 | 用來做什麼 | 得到什麼 |
|---|---|---|
| [[s-kaldun-2025-dop1r2-memory-phases]] | 在整個蕈狀體切除 Dop1R2（[[e-dopamine-receptor]]），並以抗 HA 染色驗證剪除系統 | 訓練後立刻測不受影響；2 小時記憶嫌惡由三組對照均值約 38.7 降到約 18、獎賞約 46.5 → 26.5；24 小時嫌惡約 54.5 → 11、獎賞約 45.7 → 8（皆 ※ 從圖判讀，各組 N＝12）。染色：y w 對照只有背景、Dop1R2<sup>cko</sup> 腦整個蕈狀體都亮、OK107 剪除後訊號消失（圖 1D–F） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | 在 KC 表現 GCaMP3，痕跡制約期間做鈣成像，與 TH-GAL4 標的 DAN（[[e-th-gal4]]）對照 | KC 對 CS 的反應只在 β′1、β′2 與 junction 相對減弱（第 10 回合差值 −0.09、−0.10、−0.17），γ 葉無顯著差異；KC 對電擊幾乎沒有反應（約 0.1） |
| [[s-handler-2019-dopamine-receptor-timing]] | 在 KC 軸突表現三種感測器，量 γ4/γ5 區室在順向與逆向配對下的第二傳訊者 | cAMP 在六個 ISI 全部顯著大於零（−6 至 +6 s，ΔR/R 約 0.067–0.15）；內質網鈣只在 −1.2 s 與 +0.5 s 顯著（※ 從圖判讀，見 [[c-cs-us-timing]]） |
| [[s-mao-2009-dopaminergic-neuron-types]] | 標出全部 KC 的位置，與抗 TH 染色疊圖（圖 4D） | 作為四個「哪一葉」地標中涵蓋最廣的一個，用來判定多巴胺末梢落在哪一葉 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 該頁列在 KC 的驅動品系中（與 R13F02-GAL4 並列） | 該頁沒有指明它用在哪一個實驗：？待查 |

數值見 [[numbers]]。

## 已知的問題

- **它不只標到 KC。** [[s-dylla-2017-trace-conditioning-dan-plasticity]] 指出 OK107 也標到 IPCs（製造胰島素的細胞，不屬蕈狀體）。該篇 KC 的成像表因此多出 IPCs 一列，而 IPCs 第 5 回合的差值 0.35 是全表最大（不顯著）。**這一格不是 KC，不應混入「KC 的可塑性」。**
- **「全部 KC」沒有被量化。** 五篇都沒有寫它標到幾顆、三類 KC 是否都涵蓋：？待查。
- **陰性結果的前提只在這一組被驗證。** [[s-kaldun-2025-dop1r2-memory-phases]] 的抗 HA 染色只做了 OK107 這一組，三個分葉品系（5HTR1B、c739、c305a）沒有對應的染色。反過來說，OK107 是該篇唯一有染色證據支持「真的剪掉了」的品系。
- **同一篇裡取用 KC 的品系不只一個。** [[s-pribbenow-2022-postsynaptic-plasticity]] 同時列了 R13F02-GAL4 與 OK107-GAL4；該篇沒有比較兩者標到的細胞是否相同：？待查。
- **Dylla 2017 的 KC 組沒有 mb247-DsRed 地標。** 該篇 DAN 組以 DsRed 做移動校正，OK107>GCaMP3 的 KC 組沒有帶這個轉殖基因，移動校正怎麼做該篇沒有交代：？待查。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-mushroom-body]]
- 其他 KC 品系：[[e-c739-gal4]]（α/β）、[[e-238y-gal4]]（三類 KC）、[[e-c305a-gal4]]（α′/β′）；品系原理見 [[e-split-gal4]]
- 工具：[[e-gcamp]]、[[e-epac-camp-sensor]]、[[e-dopamine-receptor]]
- 概念：[[c-mb-compartment]]、[[c-cs-us-timing]]、[[c-coincidence-detection]]
- 來源：[[s-kaldun-2025-dop1r2-memory-phases]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-pribbenow-2022-postsynaptic-plasticity]]
- 待開頁面：`e-r13f02`、`e-mb247-dsred`、`e-5htr1b-gal4`、`e-grab-da`
