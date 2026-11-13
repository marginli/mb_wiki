---
title: MBON-γ1pedc（MVP2）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, cross-domain]
confidence: medium
---

# MBON-γ1pedc（MVP2）


**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蕈狀體（mushroom body）**：果蠅腦中把氣味和好壞經驗連起來的構造。代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」（α、α′、β、β′、γ），每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ2、α1）；細胞以所在區室命名。見 [[e-mushroom-body]]、[[c-mb-compartment]]。
- **DAN、PAM、PPL1**：多巴胺神經元（dopaminergic neuron）送出代表懲罰或獎賞的多巴胺；PAM 群多傳遞獎賞，PPL1 群（Handler 2019 寫作 PPL）多傳遞懲罰。
- **MBON**：蕈狀體輸出神經元，接收 KC 的訊號、推動果蠅靠近或走開；學習改變的是 KC→MBON 突觸的強弱。
- **CS+／CS−、順向／逆向**：訓練時配了糖、電擊或 DAN 活化的氣味（CS+），與沒配的對照氣味（CS−）。順向配對＝氣味先、多巴胺後；逆向配對＝多巴胺先、氣味後。
- **PI（表現指數）、LI（學習指數）**：行為分數。一群果蠅在兩種氣味間選擇，換算成一個數；多數篇落在 −1 到 +1（Hige 2015 的刻度不同），0＝沒有偏好，正負號的意思各篇不同（見 [[c-performance-index]]）。
- **消退、再鞏固**：學會後再聞 CS+ 卻沒有糖或電擊，學到的反應減弱，叫消退（[[c-memory-extinction]]）；記憶被叫出來後暫時變得不穩定、再重新存好，叫再鞏固（[[c-memory-consolidation]]）。
- **驅動品系**：讓外加基因只在選定神經元表現的果蠅品系。GAL4 與 LexA 是兩套互不干擾的開關；split-GAL4 把 GAL4 拆成兩半（AD 與 DBD），兩半都在的細胞才有作用（[[e-split-gal4]]）。基因型寫「X/+」表示只帶一個品系的對照組。
- **活化與阻斷工具**：CsChrimson 照紅光讓神經元放電（[[e-cschrimson]]）；P2X2 遇到 ATP 讓神經元放電（[[e-p2x2]]）；shibire^ts1（shi）升溫時暫時關掉神經元的輸出（[[e-shibire-ts]]），全程維持低溫的「允許溫度對照」用來排除品系本身的效果。
- **讀數與製備**：ΔF/F0＝螢光相對刺激前基線的變化比例（0.5＝亮了 50%），以遇鈣變亮的 GCaMP 量神經元活動（[[e-gcamp]]）；離體＝把腦取出泡在養液裡做實驗（[[c-ex-vivo-explant]]），活體＝活果蠅固定後打開頭殼看。
- **電壓成像、放電率**：電壓成像（voltage imaging）是用會隨膜電壓變亮變暗的螢光蛋白（Huang 2024 用 pAce）、每秒拍 1,000 張，看得到每一次放電；放電率＝每秒放電幾次。
- **TnT**：破傷風毒素輕鏈，讓神經元無法釋放傳遞物質；**從發育期起一直作用**，不像 shibire^ts1 可以只在某段時間關掉。
- **舊名與新名**：Aso 2014a（[[s-aso-2014-mb-architecture]]）以前，蕈狀體的細胞型多用 Tanaka 2008 的舊名（MB-MP1、MB-V2α 等），同一顆細胞在不同論文裡名字不同；Aso 2014a 改以所在區室命名，並在表 1 給出新舊名對照。
- **光遺傳篩檢（Aso 2014b）**：在沒有訓練、沒有氣味時用紅光活化某型 MBON，看果蠅往照光區靠近還是走開；一條品系常同時標好幾型，只標一型就顯著的才算單型證據。
- **一氧化氮（NO）、TPM、TH 突變**：Aso 2019 發現部分 DAN 除了多巴胺還放出 NO（由 NOS 酵素合成），作用與多巴胺可以相反；TPM 是 RNA 定序的表現量單位；TH 突變背景＝不能合成多巴胺的果蠅，用來看 DAN 在沒有多巴胺時還能寫入什麼。
- **標記**：※ 推論＝本庫推得、原文沒明說；？待查＝要靠其他資料確認；「從圖判讀」＝從圖上估讀的值；「text.txt 第 N 行」＝本庫保存的論文全文文字檔的行號；「該頁」指表格同一列的來源頁。

## 是什麼

蕈狀體輸出神經元（[[e-mbon]]）的一型，樹突（收訊號的分枝）在 γ1pedc 區室，也就是 γ 葉最靠近根部的那一格（區室見 [[c-mb-compartment]]）。字尾 pedc 指柄遠端的核心部位（core of distal pedunculus；柄是 KC 軸突從萼部往前集成的一束），依 [[s-aso-2014-mb-architecture]]，它不算在 15 個區室裡，但有專屬的一型 MBON（就是這一型）與一型 DAN。完整型名 MBON-γ1pedc>α/β 也出自 Aso 2014a：「>α/β」表示它的軸突再伸到 α/β 葉。舊名 MB-MVP2（新舊名對照出自 Aso 2014a 表 1，作者註明是「最可能的對應」；Hige 2015 用這個舊名）或 MVP2（Felsenberg 2018）。依 Aso 2014a：每半腦 1 顆；樹突在同側的 γ1 與柄核心，軸突投射到兩側的 α/β 葉與對側的柄核心，在 α3 的末梢集中在表層（圖 15E、17C）；末梢對 GABA 合成酵素的抗體有反應（圖 9B，屬「推定」的傳遞物質）。依 Felsenberg 2017／2018，它放出 GABA（一種抑制性傳遞物質），活化時讓果蠅偏向「靠近」；它的軸突接到其他 MBON（M4β′、M6，見 [[e-mbon-gamma5beta2a]]）身上抑制它們，這叫前饋抑制（feedforward inhibition）。同一格的多巴胺神經元是傳遞懲罰的 [[e-ppl1-gamma1pedc]]。

## 版本與規模（標記它的品系）

| 來源 | 品系 | 用途 |
|---|---|---|
| Aso 2014a | 表 1：MB112C、MB085C、MB262B | 命名與形態 |
| Aso 2014b | MB112C（光遺傳活化只用這一條）；MB112C、MB085C、MB262B（shibire^ts 阻斷）；R12G04-LexA（與 PPL1-γ1pedc 雙色標記，圖 6K） | 逐型活化、阻斷篩檢 |
| Hige 2015 | R12G04-LexA（讓它帶 GFP，方便電極對準） | 活體全細胞記錄 |
| Felsenberg 2017 | MB112C（Methods、延伸圖 4a）；延伸圖 6i 寫 MB122C | 行為阻斷 |
| Felsenberg 2018 | MB112C-GAL4 | 活體鈣成像、解剖 |
| Huang 2024 | MB085C | TnT 阻斷（圖 4i）、CsChrimson 活化（圖 4k–m）；電壓成像用的品系在延伸表 1，未印出（？待查） |

⚠️ Felsenberg 2017 的品系名前後不一（MB112C vs MB122C，單篇自身不一致）。細胞數：Felsenberg 2018 的電顯追蹤分出左右腦各一顆（MVP2(L)、MVP2(R)）。

## 庫內誰用了它

| 來源 | 怎麼用 | 看到什麼 |
|---|---|---|
| [[s-aso-2014-mb-architecture]] | 命名與形態的原始出處（表 1、圖 9B、15E、17C） | GABA 性（推定）、每半腦 1 顆；三型「軸突送回葉內」的 MBON 之一，作者據此提出多層前饋網路的構想（純推論，沒有測功能） |
| [[s-aso-2014-mbon-valence]] | CsChrimson 光遺傳活化（MB112C，未訓練、無氣味）；shibire^ts 阻斷（MB112C、MB085C、MB262B）；MCFO 單細胞形態；與 PPL1-γ1pedc 雙色標記 | 活化 → **推動靠近**（MB112C，中位數約 0.26，※ 從圖 4 的單獨品系判讀），但光遺傳只有這一條品系；與 GABA 的 MB083C 一起活化沒有加成（約 0.24）。阻斷 → 2 小時嫌惡氣味記憶由對照的約 −0.45～−0.57 降到約 −0.25（MB112C；複篩後唯一剩下的品系），嫌惡顏色記憶由約 −0.12～−0.17 降到約 −0.03（皆 ※ 從圖判讀）；獎賞記憶與睡眠篩檢都沒有它的效果。樹突與 PPL1-γ1pedc 的末梢在 γ1、pedc 精確重疊 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 全細胞膜片鉗（[[c-whole-cell-patch-clamp]]），氣味配一顆 PPL1-γ1pedc 的光活化 | 配對氣味的放電降 80% ± 5.7%、突觸電荷降 90% ± 3.7%，至少 40 分鐘；逆向配對無效；MBON 不放電也會發生（見 [[c-kc-mbon-plasticity]]） |
| [[s-felsenberg-2017-re-evaluation]] | 在糖記憶再活化期間以 [[e-shibire-ts]] 阻斷 | 不影響消退與再鞏固；作者用它確認消退需要的是 V2 群 MBON（α、α′ 葉上的一群 MBON），不是與它相鄰的 MVP2 |
| [[s-felsenberg-2018-memory-extinction]] | 電擊訓練後活體雙光子鈣成像樹突；FAFB 電顯追蹤 | 訓練後對 CS+ 的反應比 CS− 小，消退後**仍然**比較小（中位數約 0.2 vs 0.4，從圖判讀）；接到 M6R 17 個、M6L 16 個、M4β′ 47 個突觸，接 M6 的點靠近樹突根部 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 離體腦鈣成像：TH 突變背景（不能合成多巴胺）下光活化 PPL1-γ1pedc（5 次、間隔 30 秒、最高 1.2 mW/mm²），餵或不餵 NOS 抑制劑 L-NNA；RNA 定序的預試細胞型 | 它的鈣**長時間上升**，且被 L-NNA 壓制 → 一氧化氮作用到這顆 MBON（該篇唯一的生理量測，細節在圖 5 補充圖 2，本庫未取得）。RNA 定序先拿它試水溫：三個重複、每個約 350 顆細胞，平均 5.3 µg cDNA |
| [[s-huang-2024-dopamine-memory-dynamics]] | 電壓成像量放電（寫作 MBON-γ1pedc>α/β）；TnT 阻斷後量 PPL1-α3；訓練時以 CsChrimson 持續活化（30 下 0.5 s 紅光）；模型中的 Mγ1 | 自發約 38 次／s，六型 MBON 中最高（※ 從圖判讀）；6 回合電擊訓練後對 CS+ 的反應下降、約 1 小時內恢復；它對 PPL1-α3 與 PPL1-α′2α2 有抑制性回饋，阻斷後 PPL1-α3 訓練後不再對 CS+ 增加放電；訓練時活化它 → 5 分鐘記憶正常、3 小時記憶消失（每組 12 隻）。模型拿掉這條回饋，MBON-α3 在 3 小時的改變少 36–63% |

> [[s-aso-2016-dan-cell-type-rules]] 只在圖 5B 示意圖畫出它的 GABA 前饋連結，用來解釋同時活化兩型 DAN 時的結果，沒有操作或量它，所以不列入表。

## 已知的問題

- **兩種讀法不能直接並列。** Hige 用電極量放電與電荷，誘發學習的是光活化單一顆 DAN；Felsenberg 2018 用鈣成像、真電擊、訓練後 60 分鐘量。兩者方向一致（配對氣味的反應變小），幅度不能比。
- **「推動靠近」只有一條品系的證據。** Hige 2015 引 Aso 2014b；回查 Aso 2014b，它的光遺傳活化只用了 MB112C 一條。該篇方法說單一品系的結果「只宜解讀為提示性」，圖 13 卻把它標成實心（只操作這一型就有表型），兩種標準並列沒有說明（⚠️ 單篇自身不一致）。Felsenberg 2018 引 Perisse 2016 說明它抑制 M4β′／M6。
- **Aso 2014b 的「多巴胺讓突觸變弱」是推論。** 該篇由「活化它推動靠近、同格 DAN 寫入嫌惡記憶」推論突觸變弱「最容易解釋」；直接量到突觸變弱的是 Hige 2015。
- **它的痕跡沒消，不等於下游沒變。** Felsenberg 2018 顯示，訓練留下的痕跡（MVP2 對 CS+ 的反應比 CS− 小）在消退後仍在，但下游 M6 的軸突反應被消退抵銷；只看這顆 MBON 會以為消退沒發生。
- **Huang 2024 的 CS− 也在變。** 圖 3f 中它對 CS−（沒配電擊的吸引氣味）的反應在訓練中途（Mid）也顯著下降，正文只寫 CS+ 下降，模型歸因於感覺適應。這一格與 Huang 模型「DAN 安靜時連結變強」的規則方向相反，見 [[syn-contradictions]] 1.9。
- **Huang 2024 的阻斷從發育期就開始。** TnT 不是只在訓練時關掉它，而且阻斷後 PPL1-α3 在訓練**前**對吸引氣味的下降就不見了（圖 4i）。只在訓練時操作的證據是 CsChrimson 那組，而那組只測了 3 小時一個長時間點。
- ⚠️ Felsenberg 2018 的方法表寫 MVP2→M6L 16 個突觸，圖 S4B 只畫 15 個（單篇自身不一致）。

## 相關

- 細胞：[[e-mbon]]、[[e-ppl1-gamma1pedc]]、[[e-ppl1-alpha3]]、[[e-ppl1-alpha2alpha2]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-gamma2alpha1]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-memory-extinction]]、[[c-feedforward-inhibition]]、[[c-valence-coding]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-memory-updating]]、[[t-mbon-dan-feedback]]、[[t-mbon-to-action]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]
