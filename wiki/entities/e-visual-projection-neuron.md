---
title: 視覺投射神經元（visual projection neuron, VPN）
created: 2026-11-24
updated: 2026-11-24
tags: [entity, active, visual-learning]
confidence: medium
---

# 視覺投射神經元（visual projection neuron, VPN）

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **視葉（optic lobe）**：果蠅處理影像的區域，由外而內分成髓質（medulla, ME）、小葉（lobula, LO）、小葉板（lobula plate, LoP）等神經氈；副髓質（accessory medulla, aMe）是旁邊的一小塊。
- **VPN**：本體（與樹突）在視葉、軸突伸進中央腦的神經元。對蕈狀體而言，就是把影像訊息直接送進副萼的那一類。
- **LVIN**：自己不伸進視葉、但收 VPN 輸入再轉交給 KC 的中央腦中間神經元。見 [[e-lvin]]。
- **直接／間接輸入**：VPN 直接突觸到 KC 為直接；VPN 先接 LVIN、LVIN 再接 KC 為間接。
- **副萼（accessory calyx）**：主萼之外收非嗅覺輸入的小突起，vACA（腹側）與 dACA（背側）是兩個視覺副萼。見 [[e-accessory-calyx]]。
- **單眼（ocelli）**：頭頂三個簡單眼，與複眼的視葉是平行的系統，**不是視葉神經氈**。
- **標記**：`※ 推論`＝本庫推得、原文沒明說；`？待查`＝要靠其他資料確認。

## 是什麼

**VPN 是「影像怎麼進蕈狀體」這條路的第一棒。** 約 8% 的 Kenyon 細胞收的主要不是氣味而是影像（[[s-li-2020-mb-connectome]]），而那些影像訊號有兩種送法：VPN 直接突觸到 KC，或先交給 LVIN 再轉一手。兩個視覺副萼的偏好正好相反——vACA 以直接為主、dACA 以間接為主。

**但「VPN」在庫內的兩篇來源裡不是同一個定義，這是本頁最該記住的一件事。**

| | [[s-li-2020-mb-connectome]]（hemibrain，右半腦） | [[s-ganguly-2024-visual-inputs-to-kc]]（FlyWire，左半腦） |
|---|---|---|
| 怎麼判定是 VPN | **靠形態**：本體在視葉、直接接到 KC。髓質不在 hemibrain 體積內，髓質 VPN 的身分要拿 [[e-fafb]] 或光學影像跨資料集比對 | **靠標註**：FlyWire 的 `visual_projection` 超類（Super Class），未標註者逐顆到 Codex 查補 |
| 這個定義的邊界問題 | 「在許多情況下」能確定標註髓質 VPN（**沒有給比例**）；圖 10 的圓餅另有 0.9% 歸為「無法判定來自髓質或小葉」、1.6% 歸為「離開體積、身分未定」 | 超類是標註系統的一個類，不是解剖定義：圓餅上第五片「單眼 0.9%（2 顆）」就不是視葉神經氈 |
| 同篇自陳的上限 | **"we have little definitive insight into the type of visual information conveyed by their VPN inputs"**——來源腦區確認了，編碼內容沒有 | 感受野是用眼圖法估的，而眼圖的出處在該篇發表時還是預印本（該頁第 6b 條） |

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-li-2020-mb-connectome]] | 在 hemibrain 右半腦把四個萼的輸入逐一拆成扇形，分出「VPN 直接」與「LVIN 間接」兩條路；髓質 VPN 的身分靠 [[e-fafb]] 與光學影像比對補 | **vACA：VPN 直接 46.1% ＋ LVIN 間接 24.6%；dACA 相反，LVIN 57.8% ≫ VPN 9.8%。** 同一張圖上有兩個 VPN 數：不設門檻 138 條、門檻 ≥5 突觸／單顆 KC 則只剩 49 條 |
| [[s-ganguly-2024-visual-inputs-to-kc]] | 在 FlyWire 全腦（含視葉）把每顆視覺 KC 的上游查到底，門檻一律 ≥5 突觸；再估每個 VPN 的感受野 | 左半腦 KCγ-d：**49 個直接 VPN、5,647 個突觸（75.8%）**；LVIN 的上游有 **226 個間接 VPN**（小葉 100／髓質 97／副髓質 20／小葉板 7／單眼 2）。KCαβ-p 相反：9 個 VPN、327 個突觸（16%）。**全腦 7,851 顆標為 VPN 的細胞裡只有 469 顆（約 6%）接到視覺 KC** |

各篇引用的數字見 [[numbers]]。

## 引用時的陷阱

1. **兩篇的「VPN 有幾個」不能相減也不能相除。** 不同的腦、不同的半腦、不同的資料集，連判定方式都不同（形態 vs 標註超類）。**可比的是比例，不是名單。** 而兩篇的比例確實對得上：vACA 的直接路佔視覺輸入 65.2%（[[s-li-2020-mb-connectome]]，本庫計算），dACA 只有 14.5%，而 FlyWire 對 KCαβ-p 算到 16%——這是兩篇之間最乾淨的一處交叉驗證。
2. **門檻可以把同一群細胞的數目改掉 2.8 倍。** [[s-li-2020-mb-connectome]] 圖 10 同時印著 138（不設門檻）與 49（≥5 突觸）。**引用「有幾條 VPN」一定要連門檻一起引**，這是全篇對「門檻會改變結論」最直接的示範。
3. **`visual_projection` 超類裡有不是視葉的東西。** 單眼的 2 顆被算進 [[s-ganguly-2024-visual-inputs-to-kc]] 的「依來源神經氈」圓餅，而單眼與複眼是平行系統。數量無害，但它說明那篇的 VPN 是標註類別而非解剖類別。
4. **「找得出來源腦區」不等於「知道它在編什麼」。** 兩篇都自陳這一點。把 VPN 的腦區分布引成「蕈狀體收到了髓質的某種特徵」是跨了一層。
5. **直接路與間接路大量重疊，不是兩群細胞。** [[s-ganguly-2024-visual-inputs-to-kc]] 圖 3B：相關的 239 個 VPN 裡，只走間接 79.5%、只走直接 5.4%、兩條都走 15.1%——**49 個直接 VPN 裡有 36 個（73%）同時把同一份訊號經 LVIN 再送一次**。說「直接 VPN 與間接 VPN」時，講的是路徑不是細胞群。
6. **兩篇對 KCγd 樹突上的突觸形態說法相反。** ⚠️ 矛盾 1.15（未裁決）：[[s-li-2020-mb-connectome]] 說 VPN／LVIN 打在 KCγd 上的**突觸**不呈爪狀，唯一證據是一支本庫未取得的影片；[[s-ganguly-2024-visual-inputs-to-kc]] 說有豆莢—爪接觸。詳見 [[syn-contradictions]]。

## 相關

- 配套的中繼層：[[e-lvin]]
- 進到哪裡：[[e-accessory-calyx]]、[[e-kenyon-cell]]、[[e-mushroom-body]]
- 資料集：[[e-hemibrain]]、[[e-fafb]]、[[e-neuprint]]
- 方法：[[e-nblast]]（跨連結體配對）、[[c-neurotransmitter-prediction]]（直接 VPN 全部被預測為膽鹼性）
- 主題：[[t-visual-learning-circuits]]
- 來源：[[s-li-2020-mb-connectome]]、[[s-ganguly-2024-visual-inputs-to-kc]]
- 待開頁面：`e-flywire`、`e-codex`、`e-optic-lobe`（視葉四神經氈）、`e-accessory-medulla`（副髓質與 aMe12）、`e-lc-neuron`（小葉柱狀神經元 LC15、LC24 等）、`c-receptive-field`（感受野與眼圖法）
