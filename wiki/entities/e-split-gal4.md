---
title: split-GAL4 驅動品系（split-GAL4 driver lines）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# split-GAL4 驅動品系（split-GAL4 driver lines）

## 是什麼

**驅動品系**是決定「某個外加基因只在哪些神經元表現」的果蠅品系。GAL4 是一種能開啟目標基因的蛋白；在哪些細胞裡製造它，取決於接在前面的調控序列。一般的 GAL4 品系常同時標到很多種細胞。

**split-GAL4** 把 GAL4 拆成兩半：一半負責「抓住 DNA」（DBD），一半負責「啟動表現」（AD），各由一段不同的調控序列控制。只有兩段序列都開啟的細胞，兩半才湊得成完整的 GAL4（Hige 2015 的說明）。這樣能把表現範圍縮到少數幾型、甚至一顆神經元。在本庫，它主要用來只讓特定的 [[e-dopaminergic-neuron]]（DAN）帶上光敏感通道 [[e-cschrimson]]。

另一套互不干擾的系統 LexA 常與它並用：GAL4 標 DAN，LexA 標要記錄的 MBON 或 KC。

## 版本與規模（本庫用到的品系）

| 品系 | 來源 | 兩半各由什麼控制（AD／DBD） | 標記什麼 |
|---|---|---|---|
| **MB320C** | Hige 2015 新做 | TH／22B12 | **只標一顆 PPL1-γ1pedc** |
| **MB099C** | Hige 2015 新做 | TH／73F07 | **四型 PPL1**：γ2α′1、α′2α2、α′3、α3；從不標 PPL1-γ1pedc |
| MB438B | 先前文獻（Aso et al. 2014a）中 PPL1-γ1pedc 的專一品系 | AD 插在 attP40（基因組上預先設好、供外加基因插入的固定位置） | Hige 2015 **刻意不用**，理由見下 |
| **MB042B** | Handler 2019 | R58E02／R22E04 | PAM 群（涵蓋哪些區室，論文沒列：？待查） |
| **MB504B** | Handler 2019 | 52H03／TH | PPL 群中**支配六個區室**的一部分；**是哪六個，論文沒列**：？待查 |

AD／DBD 欄取自兩篇原文的方法與基因型清單（Hige 2015 方法；Handler 2019 STAR Methods 基因型表）。TH 指合成多巴胺的酵素酪胺酸羥化酶的調控序列；22B12、73F07、R58E02、R22E04、52H03 等是調控序列片段的編號（基因型寫成「片段名-AD」「片段名-DBD」）。表中的「一顆」照 Hige 原文 a single neuron；左右腦是否各一顆，原文沒說：？待查。

**常與它並列、但不是 split-GAL4 的品系**：TH-GAL4（Hige 用作正對照，即已知應該有效、用來確認方法可行的組；Handler 與 DDC-Gal4 一起用來在 DAN 表現 VMAT-pHluorin）；R58E02-LexA（Handler 離體實驗活化 PAM，基因型表標「γ4–5 DANs」）；73F07-LexA（Handler，γ2 DAN）；Tomchik 2009 的 238Y、c739、c305a、1471、c316、GH146 都是一般 GAL4。

## 庫內誰用了它

| 來源 | 用了哪些 | 用來做什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未使用**（只用一般 GAL4，且沒有操弄 DAN） | — |
| [[s-hige-2015-heterosynaptic-plasticity]] | MB320C、MB099C | MB320C 只活化 γ1pedc 的 DAN，誘發該區 MBON 的突觸變弱；MB099C 活化鄰區 DAN，檢查多巴胺會不會越界，並用來活化 α2 區 |
| [[s-handler-2019-dopamine-receptor-timing]] | MB042B、MB504B | 行為實驗中以光活化 PAM 或 PPL；閉迴路用 MB042B 驅動 ChrimsonR |

## 已知的問題（解讀實驗的陷阱）

- **「一個品系」不等於「一型細胞」。** MB099C 同時活化四型 PPL1；TH-GAL4 標多數 PPL1、少數 PAM 以及蘑菇體以外的許多 DAN。讀到「活化 MB099C」時，要記得是四型一起放電。
- **品系不同會混進比較。** Hige 2015 比較 γ1（MB320C，一顆 DAN）與 α2（MB099C，四型 DAN）的誘發門檻，兩個品系的通道表現量與每次放出的多巴胺量可能不同。行為上，MB099C 代替電擊的效果也遠低於 MB320C（補充圖 S1F：？待查）。
- **涵蓋範圍沒有列出。** Handler 2019 的 MB504B（六個區室）與 MB042B 都沒列出支配哪些區室，而全篇的分子與突觸實驗只在 γ4 做。行為結果可能混有 γ4 以外區室的貢獻，作者也承認行為由多區室合成。
- **插入位點會互相干擾。** Hige 2015 不用 MB438B，因為它的 AD 插在 attP40，與該篇標 MBON 的 LexA 品系同一位點，可能發生 transvection（同源染色體上相同位點的調控元件互相影響），讓 GAL4 與 LexA 在同一批細胞表現；後果是光敏感通道也出現在被記錄的 MBON 上（引 Mellert & Truman 2012）。
- **同一段調控序列可出現在不同品系。** 73F07 是 Hige 的 MB099C 的 DBD，也是 Handler 標 γ2 DAN 的 LexA；25D01 在 Hige 標 MBON-γ2α′1、在 Handler 標「γ2 MBON」。※ 推論：兩篇可能標到相同或重疊的細胞，但 split-GAL4、GAL4 與 LexA 版本的表現範圍不一定相同，兩篇沒有比對：？待查（另見 [[e-mbon]]）。

## 相關

- 工具：[[e-cschrimson]]、[[e-gcamp]]
- 細胞：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]
- 概念：[[c-us-substitution]]、[[c-mb-compartment]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]
