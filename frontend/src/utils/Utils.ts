import { MenuItem } from "./Types";

export function getMenuItem({
  key,
  label,
  children,
  icon,
  type,
  noClick,
}: {
  label: React.ReactNode;
  key: React.Key;
  icon?: React.ReactNode;
  children?: MenuItem[];
  type?: "group";
  noClick?: boolean;
}): MenuItem {
  return {
    key,
    onClick: noClick ? () => {} : undefined,
    icon,
    children,
    label,
    type,
  } as MenuItem;
}