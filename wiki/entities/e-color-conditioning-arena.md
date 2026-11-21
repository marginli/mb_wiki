---
title: 四象限顏色制約場地（colour conditioning arena）
created: 2026-11-21
updated: 2026-11-21
tags: [entity, active, visual-learning]
confidence: medium
---

# 四象限顏色制約場地（colour conditioning arena）

**一座圓形走路場地，地板同時是螢幕也是電椅：下方的 LED 把整片地板打成藍色或綠色，而地板本身是一片透明的電擊格柵。** 它讓「顏色配電擊」能用和「氣味配電擊」相同的懲罰來做，是本庫兩篇顏色記憶來源共用的裝置。

## 是什麼

訓練時整片地板是單一顏色，配上（或不配上）懲罰或獎賞；測驗時地板切成四個象限、兩色交錯，數果蠅停在哪一色的象限上。果蠅是**走路**的、**成群**的（每次 30–40 隻），不是單隻拴住的飛行模擬器——這一點在跨篇比較視覺學習時很關鍵（見 [[t-visual-learning-circuits]]）。

**關鍵硬體是透明的電擊格柵。** 嗅覺制約的標準懲罰是電擊，但傳統金屬格柵不透光，而顏色刺激要從地板下方打上來。[[s-vogt-2014-shared-visual-olfactory-circuits]] 把氧化銦錫（indium tin-oxide, ITO）鍍在玻璃上、用雷射蝕出交錯的電極，於是「給電擊」與「從下方給顏色」第一次能同時做到。該篇說在此之前沒有這樣的裝置，所以**嫌惡視覺制約在此之前無法用與嗅覺相同的增強訊號來做**。

## 版本與規模

兩篇的參數完全相同（[[s-aso-2014-mbon-valence]] 的顏色記憶部分由 Vogt 與 Schnaitmann 執行），所以這是本庫少數可以直接並排絕對值的兩篇。

| 項目 | 值 | 出處 |
|---|---|---|
| 每次隻數 | 30–40 隻，雌雄混合 | 兩篇相同 |
| 藍光 | 452 或 456 nm，14.1 cd m⁻² s⁻¹（單位照原文，原文未定義） | 兩篇相同；原文列兩款 LED，未說哪些實驗用哪一款 |
| 綠光 | 520 nm，70.7 cd m⁻² s⁻¹ | 兩篇相同 |
| LED 位置 | 地板下方 144 mm | Vogt 2014 |
| 嫌惡 US | CS+ 的 60 秒內給 12 下、每下 1 秒、**AC 60 V** | 兩篇相同 |
| 電擊格柵 | 鍍在玻璃上的 ITO，雷射蝕出交錯電極；9 × 9 cm，電極道 1.6 mm、縫 0.1 mm | Vogt 2014（硬體描述只在該篇） |
| 獎賞 US | 2 M 蔗糖、乾燥濾紙；飢餓到約 20% 死亡率 | 兩篇相同 |
| 訓練與測驗 | 訓練 4 回合，最後一次訓練後**立即**測驗 90 秒 | 兩篇相同 |
| 錄影 | 90 秒、每秒 1 張 | Vogt 2014 |
| shibire<sup>ts</sup> 限制溫度 | 33 °C | 兩篇相同（Vogt 2014 的圖 8 另用 31 °C，見 [[e-shibire-ts]]） |

**分數的公式只有一篇寫出來。** [[s-aso-2014-mbon-valence]] 的 PI ＝「藍配電擊時（藍象限隻數 − 綠象限隻數）÷ 總隻數」與「綠配電擊時（綠象限隻數 − 藍象限隻數）÷ 總隻數」兩者的平均（圖 8A 圖說）。[[s-vogt-2014-shared-visual-olfactory-circuits]] 稱它為學習指數（learning index, LI），**公式沒有寫出來**，只寫是兩組互換 CS+ 之間視覺刺激偏好的差、逐影格計算，並引 Schnaitmann et al. 2010。見 [[c-performance-index]]。

數值見 [[numbers]]。

## 庫內誰用了它

| 來源 | 用來量什麼 | 得到什麼 |
|---|---|---|
| [[s-vogt-2014-shared-visual-olfactory-circuits]] | 整篇的主裝置：電壓劑量曲線、三條胺類品系、兩條 DAN 品系、受體突變與救援、八條 KC 品系、訓練／測驗時段拆分；並在同一篇裡與 T 迷宮的嗅覺記憶並排 | 顏色記憶需要 PAM 群（獎賞）與 PPL1 四型（懲罰）、KC 中的 DopR、KC 的 γ 葉；α′/β′ 只管氣味。電壓—記憶曲線在約 30 V 達高原，故一律用 60 V |
| [[s-aso-2014-mbon-valence]] | 以 shibire<sup>ts</sup> 全程阻斷，逐型篩檢「顏色記憶需要哪些 MBON」 | 嫌惡顏色記憶需要 MBON-γ1pedc>α/β（MB112C ＋ MB262B 兩條品系確認），與嫌惡**氣味**記憶同一型；阻斷同格的 PPL1-γ1pedc（MB438B）也造成強烈缺陷。獎賞顏色記憶需要 5 條品系涵蓋的麩胺酸與乙醯膽鹼 MBON |

## 已知的問題

- **兩色的亮度相差約五倍（14.1 對 70.7），而是否做過等亮度校正，[[s-aso-2014-mbon-valence]] 沒有說明：？待查。** 這表示「果蠅選藍或選綠」有可能部分是亮度偏好，而不是純顏色偏好。兩篇都以「兩組互換 CS+ 相減」來抵銷固定的顏色偏好，這抵銷得掉**對兩色的共同偏好**，抵銷不掉偏好與學習之間的交互作用。
- **視覺側的分數本來就小，所以陰性結果的偵測力低。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 的視覺 LI 對照落在 +0.09 到 +0.22（糖）與 −0.10 到 −0.24（電），而同一篇的**嗅覺**對照約 −0.63，相差約六倍；[[s-aso-2014-mbon-valence]] 的嫌惡顏色記憶對照只有約 −0.12 到 −0.17。兩篇關於「某一群細胞不需要」的結論都建立在這個窄範圍裡的陰性結果上。
- **跨模態比較時增強訊號其實不同。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 的顏色實驗用 AC 60 V，同篇的 T 迷宮嗅覺實驗用 **DC 100 V**；而糖那一側根本沒有並排的嗅覺實驗（該篇沒有做欲求嗅覺制約）。摘要把「共用增強刺激」當成設計優勢，在電擊這一項上並不精確。
- **樣本數。** [[s-aso-2014-mbon-valence]] 的顏色記憶（圖 8、9）在正文、方法與圖說中都**沒有報告 n**（該頁已搜過全文）。[[s-vogt-2014-shared-visual-olfactory-circuits]] 的 n 逐圖都有（多為 6–19）。
- **測驗只到立即，最長 30 分鐘。** 兩篇都在訓練後立即測；[[s-vogt-2014-shared-visual-olfactory-circuits]] 最長量到 30 分鐘保留，嫌惡視覺 LI 由立即的 −0.18 掉到 −0.08。顏色記憶的 2 小時與 24 小時曲線本庫沒有來源（見 [[syn-contradictions]]）。
- **場地沒有情境變換的對照，除了一組。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 的圖 5B 刻意取消訓練與測驗之間的情境變換、並加入操作成分，結果仍需要蕈狀體；但那是該篇唯一一組這樣的實驗。

## 相關

- 主題：[[t-visual-learning-circuits]]
- 其他行為裝置：[[e-t-maze]]（氣味二選一）、[[e-olfactory-arena]]（氣味四象限）
- 工具：[[e-shibire-ts]]、[[e-dtrpa1]]
- 概念：[[c-performance-index]]、[[c-appetitive-memory]]、[[c-us-substitution]]、[[c-nonassociative-learning]]
- 來源：[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-aso-2014-mbon-valence]]
- 待開頁面：`e-ito-shock-grid`（透明的氧化銦錫電擊格柵，本庫只有 Vogt 2014 描述過它的規格）
