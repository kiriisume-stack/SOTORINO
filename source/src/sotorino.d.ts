// SOTORINO — window.Sotorino. Every component is a function returning an HTML string.
// Render with Sotorino.render(element, html) so behaviour (slider, search, tabs, TOC, favorites, drawer) is bound.

/** Article id from Sotorino.data.articles, or an article object. */
type ArticleRef = string | Article;
interface Article { id: string; cat: CategoryId; title: string; desc: string; img: ImageKey; date: string; updated?: string; path: string; tags?: string[]; }
type CategoryId = 'garden' | 'turf' | 'exterior' | 'carport' | 'deck' | 'equipment' | 'reform' | 'realestate' | 'money' | 'life';
/** A key in Sotorino.images (swap photos with Sotorino.setImages). Unknown keys render a labelled placeholder. */
type ImageKey = string;

interface LogoProps { current?: boolean }
interface IconProps { name: string; className?: string }
interface ButtonProps { label: string; href?: string; variant?: 'primary' | 'accent' | 'outline' | 'ghost-light'; size?: 'sm'; block?: boolean; arrow?: boolean; iconLeft?: string; rel?: string }
type CategoryLabelProps = CategoryId | { cat: CategoryId };
interface PRLabelProps { dark?: boolean; text?: string }
interface TagListProps { tags: string[] }
interface SearchProps { id?: string; placeholder?: string }
interface HeaderProps { /** nav id of the current section, 'home' on the top page */ active?: string }
interface BreadcrumbProps { items: { name: string; path?: string }[] }
interface FooterProps {}
interface HeroSliderProps { slides?: { img: ImageKey; alt: string; article: string }[]; title?: string; lead?: string }
interface CategoryTilesProps { categories?: { id: string; name: string; sub: string; img: ImageKey; path: string }[] }
interface SectionHeadingProps { title: string; en?: string; more?: string; id?: string; light?: boolean; level?: 'h2' | 'h3' }
interface ArticleCardProps { article: ArticleRef; variant?: 'grid' | 'row' | 'feature' | 'mini'; desc?: boolean; headingLevel?: string }
interface FeatureGridProps { /** first = large feature, next three = rows */ items?: string[] }
interface CTABannerProps { title?: string; text?: string; cta?: string; href?: string; img?: ImageKey; sponsored?: boolean }
interface RankingProps { mode?: 'ranking' | 'editor'; id?: string; title?: string; limit?: number; items?: string[]; ranking?: { source: string; periods: { id: string; name: string; items: string[] }[] } }
interface GuideCardProps { title?: string; text?: string; href?: string }
interface PillarGuideProps { guide?: { title: string; text: string; path: string; chapters: { no: string; name: string; desc: string; path: string }[] } }
interface PurposeNavProps { img?: ImageKey }
interface ArticleHeaderProps { article: ArticleRef; lead?: string; heroAlt?: string; caption?: string; pr?: boolean }
interface SummaryBoxProps { items: string[]; title?: string }
interface TableOfContentsProps { items: { id: string; text: string; children?: { id: string; text: string }[] }[] }
/** Block list; see README of ArticleBody for every block type. */
type ArticleBodyProps = Array<{ type: string; [key: string]: unknown }>;
interface IconFeatureGridProps { items: { img: ImageKey; icon: string; title: string; desc: string; alt?: string }[] }
interface TypeGridProps { items: { img: ImageKey; name: string; desc: string; path?: string; alt?: string }[] }
interface CompareTableProps { caption: string; head: string[]; rows: { cells: string[]; pick?: boolean }[]; note?: string }
interface StatSummaryProps { items: { label: string; value: string; unit?: string; note?: string }[] }
interface NoteBoxProps { kind?: 'point' | 'caution' | 'info'; title?: string; html?: string; items?: string[] }
interface StepsProps { items: { title: string; desc: string; time?: string }[] }
interface ProsConsProps { pros: string[]; cons: string[]; proTitle?: string; conTitle?: string }
interface ChecklistProps { title?: string; items: { text: string; sub?: string }[] }
interface FAQProps { items: { q: string; a: string }[] }
interface InlineRelatedProps { article: ArticleRef; label?: string }
interface NextStepsProps { items?: { step: string; icon: string; title: string; desc: string; path: string; go: string }[] }
interface ProductCardsProps { title?: string; criteria?: string; items: { img: ImageKey; name: string; forWhom: string; spec: [string, string][]; price: string; priceNote?: string; shops: { name: string; href?: string }[] }[] }
interface ContractorCTAProps { title?: string; points?: string[]; cta?: string; href?: string }
interface AuthorBoxProps { name?: string; role?: string; bio?: string; initial?: string; sources?: string[] }
interface TopicClusterProps { current?: string; compact?: boolean; uid?: string; series?: { name: string; path: string; items: { id: string | null; name: string }[] } }
interface RelatedArticlesProps { items: string[]; title?: string; list?: boolean; more?: string; moreLabel?: string; uid?: string }
interface ConsultBoxProps { title?: string }

declare const Sotorino: {
  config: { base: string; logoSrc: string | null; favoritesKey: string; autoplayMs: number };
  images: Record<ImageKey, string>;
  setImages(map: Record<ImageKey, string>): void;
  data: Record<string, any>;
  render(el: Element, html: string): Element;
  mount(root?: ParentNode): ParentNode;
  icon(name: string, className?: string): string;
  tocFrom(blocks: ArticleBodyProps): TableOfContentsProps['items'];
  searchArticles(q: string): Article[];
  seo: { articleJsonLd(a: Article, o?: object): object; faqJsonLd(items: FAQProps['items']): object; breadcrumbJsonLd(items: BreadcrumbProps['items'], origin?: string): object };
  Logo(p?: LogoProps): string; Button(p: ButtonProps): string; CategoryLabel(p: CategoryLabelProps): string; PRLabel(p?: PRLabelProps): string; TagList(p: TagListProps): string; Search(p?: SearchProps): string;
  Header(p?: HeaderProps): string; Breadcrumb(p: BreadcrumbProps): string; Footer(): string;
  HeroSlider(p?: HeroSliderProps): string; CategoryTiles(p?: CategoryTilesProps): string; SectionHeading(p: SectionHeadingProps): string; ArticleCard(p: ArticleCardProps): string; FeatureGrid(p?: FeatureGridProps): string; CTABanner(p?: CTABannerProps): string; CatalogCard(p?: object): string; Ranking(p?: RankingProps): string; GuideCard(p?: GuideCardProps): string; PillarGuide(p?: PillarGuideProps): string; PurposeNav(p?: PurposeNavProps): string; LatestGrid(p?: { items?: string[]; cols?: 3 | 4; desc?: boolean }): string;
  ArticleHeader(p: ArticleHeaderProps): string; SummaryBox(p: SummaryBoxProps): string; TableOfContents(p: TableOfContentsProps): string; ArticleBody(blocks: ArticleBodyProps): string; IconFeatureGrid(p: IconFeatureGridProps): string; TypeGrid(p: TypeGridProps): string; CompareTable(p: CompareTableProps): string; StatSummary(p: StatSummaryProps): string; NoteBox(p: NoteBoxProps): string; Steps(p: StepsProps): string; ProsCons(p: ProsConsProps): string; Checklist(p: ChecklistProps): string; FAQ(p: FAQProps): string; InlineRelated(p: InlineRelatedProps): string; NextSteps(p?: NextStepsProps): string; ProductCards(p: ProductCardsProps): string; ContractorCTA(p?: ContractorCTAProps): string; AuthorBox(p?: AuthorBoxProps): string; TopicCluster(p?: TopicClusterProps): string; RelatedArticles(p: RelatedArticlesProps): string; ConsultBox(p?: ConsultBoxProps): string;
  TopPage(): string; ArticlePage(p?: { article?: object }): string; CategoryPage(): string;
};
