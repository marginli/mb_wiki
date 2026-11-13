---
title: Kenyon 細胞（Kenyon cell, KC）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: high
---

# Kenyon 細胞（Kenyon cell, KC）

## 是什麼

[[e-mushroom-body]]（蕈狀體）的主體神經元，負責在蕈狀體裡代表氣味。KC 的樹突在萼部（calyx）接收嗅覺輸入，軸突沿著「葉」往外延伸，經由突觸（神經元之間傳訊號的接點）把訊號交給蕈狀體輸出神經元（[[e-mbon]]）。多巴胺神經元（[[e-dopaminergic-neuron]]）的末梢就伸在這些突觸旁邊，本庫各篇都認為學習改變的是「KC → MBON」這個突觸（見 [[c-kc-mbon-plasticity]]）。

**數量**：約 2,000 顆（每半腦）。庫內自己計數的是 [[s-aso-2014-mb-architecture]]：以 nlsLacZ 標核、電腦輔助計數，七型逐型為 γd 約 75、γ main 約 600、α′/β′ap 約 210、α′/β′m 約 140、α/βp 約 90、α/βs 約 500、α/βc 約 400，加總 2,015。Aso 2016 引言「~2000」（引 Laurent & Naraghi 1994、Perez-Orive et al. 2002）與 Cohn 2015 引言「~2,000」都是轉述，沒有自己計數。

**三類**（依 [[s-tomchik-2009-camp-dynamics]]）：α/β、α′/β′、γ。前兩類的軸突分岔成垂直葉與水平葉，γ 類只有水平的 γ 葉。所以「量 α 葉」就是量 α/β KC 的軸突。[[s-aso-2014-mb-architecture]] 把這三類再細分成上列七型，依據是樹突在主萼還是副萼、軸突走葉的哪一層。

**稀疏編碼**（sparse coding）：每種氣味只活化一小群 KC，不同氣味用到的 KC 大多不重疊（Hige 2015）。好處是改動一種氣味的突觸，較不會波及另一種；但只要有重疊，就會有一部分波及。Hige 2015 的資料：每隻果蠅圈出約 82 顆 KC 細胞體，對某一氣味有反應的約佔 12–13%（本庫推算）；對 3-辛醇（OCT）有反應的 KC 中約 30%、對 4-甲基環己醇（MCH）有反應的 KC 中約 33% 對兩者都反應（數字見 [[numbers]]）。

## 庫內誰用了它

| 來源 | 標記 KC 的驅動品系 | 量 KC 的哪個部位、量什麼 | 怎麼刺激 KC |
|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | GAL4：238Y（三類都標）、c739（α/β）、c305a（α′/β′）、1471（γ） | 軸突（α、α′、γ 葉）與樹突（萼部）；cAMP（[[e-epac-camp-sensor]]）與鈣（[[e-gcamp]]） | 乙醯膽鹼 30 mM 噴萼部，模擬氣味 |
| [[s-gervasi-2010-pka-dynamics]] | GAL4：238Y（[[e-238y-gal4]]，三類都標，但不只表現於蕈狀體） | 活體：萼部（樹突）與 α、β、γ 葉（軸突）的 PKA（感測器 AKAR2）；α′、β′ 葉太暗、量不到；細胞體對 forskolin 幾乎不反應，之後不量 | 浴灌藥物：forskolin、IBMX、多巴胺、章魚胺、乙醯膽鹼（模擬氣味） |
| [[s-hige-2015-heterosynaptic-plasticity]] | LexA（另一套表現系統，見表下說明；該篇的 GAL4 已用來讓 DAN 帶上光敏感通道）：R13F02-LexA（全部 KC）表現 GCaMP6f；R14H06-LexA 標 γ KC | **細胞體**的鈣反應，確認「配對」（讓氣味與 DAN 活化同時出現，即實驗中的學習操作）前後 KC 對氣味的反應沒有改變；γ KC 是否變得較難放電（興奮性），以電極直接記錄的測試在補充圖 S7：？待查 | 真的氣味（OCT、MCH） |
| [[s-handler-2019-dopamine-receptor-timing]] | GAL4：OK107（論文標為「KCs」，涵蓋哪幾類沒有寫：？待查） | **軸突**在 γ4/γ5 區室的 cAMP、內質網鈣（細胞內儲鈣小倉庫放出的鈣）與收到的多巴胺；KC 軸突上的兩種多巴胺受體 DopR1、DopR2 | 乙醯膽鹼 10 mM 以離子導入（用電流把藥從玻璃細針推出）送到萼部，脈衝 500 ms |
| [[s-cohn-2015-coordinated-neuromodulation]] | 讓全部 γ KC 表現 sytGCaMP（啟動子名稱 ？待查）；另以稀疏標記只標少數幾顆 | **突觸前末梢**的鈣，逐格比較同一條軸突；KC 本身的膜電位與放電（膜片鉗，補充圖 S6B：？待查） | 活體用真的氣味；離體以乙醯膽鹼離子導入萼部 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | α/β KC：c739（[[e-c739-gal4]]）、MB008B；KC：MB247 | **沒有量 KC 活動**；以 shibire^ts 阻斷 α/β KC 輸出、以 RNAi 在 α/β KC 降低 DopR1（[[e-dopamine-receptor]]） | 真的氣味與糖（行為） |
| [[s-minnick-2026-untrained-connectome]] | **不是實驗，是模擬**：BANC 連結體中的 4,504 顆 KC，每顆為一個 LIF 單元 | 活化比例與兩種氣味的重疊度（見 [[c-sparse-coding]]）；KC→MBON 的 28,415 個突觸中 8,377 條可塑 | 模擬的氣味驅動受體神經元；增強訊號為外加的純量 |
| [[s-aso-2014-mb-architecture]] | 七型各有自己的 split-GAL4（表 1；圖 6、圖 7 的單細胞影像出自 MB463B、MB418B、MB369B、MB469B、MB371B） | **不量活性，只看形態**：以 nlsLacZ 標核在高解析（0.1 µm 等向體素）下電腦輔助計數，以 MCFO 看單顆 KC 的軸突分枝 | 不刺激（固定腦） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | GAL4：OK107（全部 KC，也標到製造胰島素的 IPCs） | 活體；九個區室內 KC 軸突的細胞質鈣（GCaMP3），每格是數百顆 KC 的總和 | 真的氣味（BUT、MCH、礦物油）與足部電擊 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | RNA 定序分選三類 KC（每個重複挑 1,000–2,500 顆）；以 MB247-switch 在成蟲期於 KC 誘發 Gycβ100B-shRNA 或 *scrib*-shRNA | **不量活性**：量 KC 的轉錄本（KC γ 的 sGC 兩個次單元 Gycα99B 99、Gycβ100B 42 TPM，其他鳥苷酸環化酶低得多）與敲低後的記憶 | 不刺激 KC；刺激的是 DAN（紅光） |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**；GMR14H06-LexA（表現 TNTe 阻斷或 CsChrimson 活化）、GMR14H06-GAL4（表現 Kir2.1 慢性抑制） | 未量 KC 本身，量的是下游 MBON-m1 與 CN-33 的鈣 | 紅光同時活化全部 KC（作者引 Honegger 2011 說自然氣味只活化約 5%）；或把 KC 關掉，看側角通路單獨的效果 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | GAL4：R13F02（全部 KC，表現 Shi）、OK107（離體對照，表現 GCaMP6f 或 SynaptoPhluorin）、MB369B（稀疏的 α′/β′ KC） | 離體：軸突的鈣與囊泡釋放，用來確認 KC 沒有被外加的乙醯膽鹼活化；活體：α′3 區室內 α′/β′ KC 的氣味反應 | **刻意繞過 KC**：乙醯膽鹼噴在 MBON 樹突上（加大到 8–14 psi、150–525 ms，KC 仍無反應）。行為實驗則在訓練時以 Shi 阻斷 KC 的輸出 |

> 「驅動品系」是決定外加基因只在哪些細胞表現的果蠅品系；GAL4 與 LexA 是兩套互不干擾的系統，所以同一隻果蠅可以用一套標 DAN、另一套標 KC 或 MBON。split-GAL4 見 [[e-split-gal4]]。

## 已知的問題

- **沒有一篇直接量到 KC 末梢「送出多少訊號」。** Tomchik 量的是軸突內部的 cAMP 與鈣；Hige 量的是細胞體（離突觸很遠），排除的是「KC 整體變了」，排除不了「末梢局部少送了」；Handler 量的是軸突內的第二傳訊者（受體被活化後在細胞內傳遞訊號的小分子，如 cAMP）；Cohn 2015 量到了突觸前末梢的鈣，而且看到它隨多巴胺逐格改變，但鈣仍不是釋放量，配對後的末梢鈣也沒有量（見 [[c-presynaptic-calcium]]）。突觸的改變在 KC 這一側（突觸前）還是 MBON 那一側（突觸後），本庫各篇都沒有定案（見 [[t-dopamine-to-plasticity]]）。
- **同一條軸突在不同區室的末梢可以不一樣。** Cohn 2015：活體中同一條 γ KC 軸突在 γ2/γ3 的末梢反應強、γ4/γ5 弱；所以「KC 對某氣味的反應」要說清楚量的是哪一格。
- **細胞體與軸突的結果不能互相代替。** Hige 2015 討論中引 Boto et al. 2014：同一個 γ1 區，氣味與 DAN 活化配對之後，Boto 在 KC 軸突末梢看不到鈣變化；Hige 卻量到 MBON 對該氣味收到的突觸電流總量比配對前少約九成。
- **各篇用的驅動品系涵蓋的 KC 類別不同**（238Y 三類、R13F02 全部、OK107 未說明、c739 與 MB008B 只有 α/β），跨篇比較 KC 反應的絕對大小沒有意義。[[s-kaldun-2025-dop1r2-memory-phases]] 用 OK107（全蕈狀體）、5HTR1B（γ）、c739（α/β）、c305a（α′/β′）把受體的需求定位到**葉**，沒有做到區室層級，所以不能和 Hige 2015、Aso 2016 的區室結果並排；而且它只驗證了 OK107 那一組的剪除效率。
- **七型不是終點。** [[s-aso-2014-mb-architecture]] 自己寫明 α/βc 還可以再分內核與外核（引 Tanaka 2008），但界線不明確，他們也做不出只標外核的品系（圖 7C 圖說）。所以「七型」受限於當時的遺傳工具。
- **刺激方式不同**：Tomchik、Handler 用乙醯膽鹼滴萼部模擬氣味，Hige 用真的氣味。滴藥的時間長度與濃度不等於真實氣味。

## 相關

- 結構：[[e-mushroom-body]]；下游：[[e-mbon]]；調控：[[e-dopaminergic-neuron]]
- 感測器：[[e-gcamp]]、[[e-epac-camp-sensor]]；工具：[[e-split-gal4]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-coincidence-detection]]、[[c-camp-signaling]]、[[c-mb-compartment]]、[[c-presynaptic-calcium]]
- 品系與受體：[[e-c739-gal4]]、[[e-dopamine-receptor]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-aso-2014-mb-architecture]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-kaldun-2025-dop1r2-memory-phases]]
