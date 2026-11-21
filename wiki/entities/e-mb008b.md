---
title: MB008B split-GAL4 品系（MB008B）
created: 2026-11-21
updated: 2026-11-21
tags: [entity, active, cross-domain]
confidence: medium
---

# MB008B split-GAL4 品系（MB008B）

**標記 α/β 葉 Kenyon 細胞的 split-GAL4 品系，庫內兩篇用它，一篇在嗅覺側、一篇在視覺側。** 它是 Janelia 那批蕈狀體 split-GAL4 的一員（[[e-split-gal4]]），由 [[s-aso-2014-mb-architecture]] 做品系評估。

## 是什麼

split-GAL4 把轉錄活化子切成兩半，只有兩段調控序列都作用到的細胞才會打開外加基因，所以標記範圍比一般 GAL4 窄。MB008B 的構築式由 [[s-vogt-2014-shared-visual-olfactory-circuits]] 寫出：

> **R13F02-p65ADZp（attP40）／R44E04-ZpGAL4DBD（attP2）**，標記 α/β 葉的 KC。

同一批的其他四條（MB504B、MB010B、MB009B、MB186B）見 [[e-split-gal4]]；本頁只處理 MB008B。

## 版本與規模

| 來源 | 它對 MB008B 寫了什麼 |
|---|---|
| Vogt 2014 | 「MB008B-GAL4 標記 α/β 葉」（圖 7A 圖說）。影像為**部分投影**（partial projections），比例尺 100 µm。給出完整構築式 |
| Ichinose 2015 | 「標 α/β KC」，品系來源註明 Aso et al. 2014a。與 [[e-c739-gal4]] 並用為第二條 α/β KC 品系 |

**兩篇都沒有量它標了幾顆 KC**：？待查。數值見 [[numbers]]。

## 庫內誰用了它

| 來源 | 讓細胞帶上什麼 | 得到什麼 |
|---|---|---|
| [[s-vogt-2014-shared-visual-olfactory-circuits]] | UAS-shi<sup>ts1</sup>，全程阻斷 α/β KC 的輸出 | **兩種顏色記憶都只剩約 55%**（由圖 7B 柱高計算），但都未達顯著；正文補一句「有受損的傾向」，圖 7B 的圖說與圖 9 的模型圖則把它歸到「不需要」那一邊。n ＝ 8–23 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | (1) UAS-shi<sup>ts1</sup>（阻斷 α/β KC 輸出）；(2) UAS-DopR1-RNAi（降低 α/β KC 上的多巴胺受體） | (1) 訓練時阻斷使獎賞長期記憶降到約 0.26（兩對照約 0.41 與 0.44），n ＝ 18–19。(2) 降低 DopR1 後長期記憶約 0（對照約 0.43–0.53），與 c739 的約 0.13 同向——這是該篇「多巴胺作用在 KC 而非 MBON」的主要依據之一 |

## 已知的問題

- **它在兩篇裡的角色相反，而這個對比正是它值得單獨一頁的原因。** 在嗅覺的獎賞長期記憶上，阻斷它造成顯著缺陷（Ichinose 2015）；在顏色記憶上，同樣的阻斷只剩約 55% 卻不顯著（Vogt 2014）。**兩者不是矛盾**：一邊是嗅覺、24 小時的長期記憶，一邊是視覺、立即測的記憶，而且視覺側的基準分數小六倍、偵測陰性結果的能力低（見 [[c-performance-index]] 與 [[e-color-conditioning-arena]]）。引用「α/β 不參與」時要連模態與時間點一起引。
- **「55% 不顯著」與「0% 沒有效果」被歸成同一類。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 圖 7B 裡 MB186B（α′/β′）的殘存是 107–111%（真的完全沒效果），MB008B 是約 55%；論文一律寫成「沒有顯著降低」。**這兩件事在量上差很多。**
- **split-GAL4 的「專一」是靠影像宣告的，而那張影像是部分投影。** [[s-vogt-2014-shared-visual-olfactory-circuits]] 圖 7A 明寫是 partial projections，卻用來支持「專一標記不同的葉」；同篇對舊品系 201y 做了 MB247-GAL80 對照，對五條 split-GAL4 則沒有任何等價對照。
- **樣本數不平衡會讓同一個星號代表不同的效果量。** [[s-ichinose-2015-reward-recurrent-circuit]] 的 c739 兩組 n ＝ 7、MB008B 兩組 n ＝ 18–19，c739 的損害較大卻同為一顆星。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-mushroom-body]]
- 其他 α/β KC 品系：[[e-c739-gal4]]、[[e-mb247-gal4]]（α/β＋γ）；品系原理與其他四條 split-GAL4 見 [[e-split-gal4]]
- 工具與受體：[[e-shibire-ts]]、[[e-dopamine-receptor]]
- 概念：[[c-mb-compartment]]、[[c-performance-index]]、[[c-acquisition-vs-retrieval]]
- 裝置：[[e-color-conditioning-arena]]、[[e-t-maze]]
- 來源：[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2014-mb-architecture]]（品系評估）
- 待開頁面：`e-mb009b`、`e-mb010b`、`e-mb186b`、`e-17d-gal4`、`e-201y-gal4`
